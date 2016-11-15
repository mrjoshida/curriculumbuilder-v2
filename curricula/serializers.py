from rest_framework import serializers

from curricula.models import Unit, Curriculum
from lessons.models import Lesson, Annotation


class LessonSerializer(serializers.ModelSerializer):
    unit = serializers.SerializerMethodField()
    unit_number = serializers.SerializerMethodField()

    class Meta:
        model = Lesson
        # depth = 1
        fields = ('title', 'number', 'unit', 'unit_number', 'description')

    def get_unit(self, obj):
        return obj.unit.title

    def get_unit_number(self, obj):
        return obj.unit.number


class UnitSerializer(serializers.ModelSerializer):
    lessons = serializers.SerializerMethodField()

    class Meta:
        model = Unit
        # depth = 1
        fields = ('title', 'slug', 'description', 'number', 'curriculum', 'lessons')

    def get_lessons(self, obj):
        lessons = obj.lessons
        serializer = LessonSerializer(lessons, many=True)
        return serializer.data


class CurriculumSerializer(serializers.ModelSerializer):
    units = serializers.SerializerMethodField()

    class Meta:
        model = Curriculum
        # depth = 2
        fields = ('title', 'slug', 'description', 'units')

    def get_units(self, obj):
        units = obj.units
        serializer = UnitSerializer(units, many=True)
        return serializer.data


class Range():
    def __init__(self, start, end, startOffset, endOffset):
        self.start = start
        self.end = end
        self.startOffset = startOffset
        self.endOffset = endOffset


class RangeSerializer(serializers.BaseSerializer):
    start = serializers.CharField(max_length=50)
    end = serializers.CharField(max_length=50)
    startOffset = serializers.IntegerField()
    endOffset = serializers.IntegerField()

    def to_representation(self, obj):
        ranges = Range(obj[0], obj[1], obj[2], obj[3])
        return [ranges.__dict__]

    def to_internal_value(self, data):
        try:
            start = data[0]['start']
            end = data[0]['end']
            startOffset = data[0]['startOffset']
            endOffset = data[0]['endOffset']
            return Range(start, end, startOffset, endOffset)
        except AttributeError:
            return AttributeError


'''
class AnnotationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Annotation
        fields = ('pk', 'owner', 'lesson', 'annotator_schema_version', 'text', 'quote', 'uri', 'range_start',
				        				'range_end', 'range_startOffset', 'range_endOffset')
'''


class AnnotationSerializer(serializers.Serializer):
    id = serializers.CharField(label="id", required=False)
    annotator_schema_version = serializers.CharField(max_length=8, allow_blank=True, required=False)
    created = serializers.CharField(allow_blank=True, required=False)
    updated = serializers.CharField(source='modified', allow_blank=True, required=False)
    text = serializers.CharField()
    quote = serializers.CharField()
    uri = serializers.CharField(max_length=100, min_length=None, allow_blank=True, required=False)
    ranges = RangeSerializer()
    user = serializers.CharField(source='owner', label='user', required=False)
    lesson = serializers.CharField()

    def update(self, instance, validated_data):
        instance.annotator_schema_version = validated_data.get('annotator_schema_version',
                                                               instance.annotator_schema_version)
        instance.text = validated_data.get('text', instance.text)
        instance.quote = validated_data.get('quote', instance.quote)
        instance.uri = validated_data.get('uri', instance.uri)

        # Unpacking the ranges dict into 4 fields in instance.
        try:
            ranges = validated_data['ranges']
            instance.range_start = ranges.start
            instance.range_end = ranges.end
            instance.range_startOffset = ranges.startOffset
            instance.range_endOffset = ranges.endOffset
        except KeyError:
            print "No ranges array passed to AnnotationSerializer."

        instance.save()
        return instance

    def create(self, validated_data):
        annotation = dict()
        annotation['owner'] = self.context['request'].user
        annotation['quote'] = validated_data.get('quote')
        annotation['text'] = validated_data.get('text')
        annotation['uri'] = validated_data.get('uri')
        annotation['lesson'] = Lesson.objects.get(pk=validated_data.get('lesson'))

        # Unpacking the ranges dict into 4 fields in instance.
        try:
            ranges = validated_data['ranges']
            annotation['range_start'] = ranges.start
            annotation['range_end'] = ranges.end
            annotation['range_startOffset'] = ranges.startOffset
            annotation['range_endOffset'] = ranges.endOffset
        except KeyError:
            print "No ranges array passed to AnnotationSerializer."

        return Annotation.objects.create(**annotation)
