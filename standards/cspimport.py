import re

cspframework = {}
cspframework["1.1"] = "1.1 Creative development can be an essential process for creating computational artifacts.";
cspframework["1.1.1"] = "1.1.1 Apply a creative development process when creating computational artifacts. [P2]";
cspframework[
    "1.1.1A"] = "1.1.1A A creative process in the development of a computational artifact can include, but is not limited to, employing nontraditional, nonprescribed techniques; the use of novel combinations of artifacts, tools, and techniques; and the exploration of personal curiosities.";
cspframework[
    "1.1.1B"] = "1.1.1B Creating computational artifacts employs an iterative and often exploratory process to translate ideas into tangible form.";
cspframework[
    "1.2"] = "1.2 Computing enables people to use creative development processes to create computational artifacts for creative expression or to solve a problem.";
cspframework["1.2.1"] = "1.2.1 Create a computational artifact for creative expression. [P2]";
cspframework[
    "1.2.1A"] = "1.2.1A A computational artifact is anything created by a human using a computer and can be, but is not limited to, a program, an image, audio, video, a presentation, or a web page file.";
cspframework[
    "1.2.1B"] = "1.2.1B Creating computational artifacts requires understanding and using software tools and services.";
cspframework[
    "1.2.1C"] = "1.2.1C Computing tools and techniques are used to create computational artifacts and can include, but are not limited to, programming IDEs, spreadsheets, 3D printers, or text editors.";
cspframework[
    "1.2.1D"] = "1.2.1D A creatively developed computational artifact can be created by using nontraditional, nonprescribed computing techniques.";
cspframework[
    "1.2.1E"] = "1.2.1E Creative expressions in a computational artifact can reflect personal expressions of ideas or interests.";
cspframework[
    "1.2.2"] = "1.2.2 Create a computational artifact using computing tools and techniques to solve a problem. [P2]";
cspframework["1.2.3C"] = "1.2.3C Combining or modifying existing artifacts can show personal expression of ideas.";
cspframework[
    "1.2.2A"] = "1.2.2A Computing tools and techniques can enhance the process of finding a solution to a problem.";
cspframework[
    "1.2.2B"] = "1.2.2B A creative development process for creating computational artifacts can be used to solve problems when traditional or prescribed computing techniques are not effective.";
cspframework["1.2.3"] = "1.2.3 Create a new computational artifact by combining or modifying existing artifacts. [P2]";
cspframework[
    "1.2.3A"] = "1.2.3A Creating computational artifacts can be done by combining and modifying existing artifacts or by creating new artifacts.";
cspframework[
    "1.2.3B"] = "1.2.3B Computation facilitates the creation and modification of computational artifacts with enhanced detail and precision.";
cspframework["1.2.4"] = "1.2.4 Collaborate in the creation of computational artifacts. [P6]";
cspframework[
    "1.2.4A"] = "1.2.4A A collaboratively created computational artifact reflects effort by more than one person.";
cspframework["1.2.4B"] = "1.2.4B Effective collaborative teams consider the use of online collaborative tools.";
cspframework[
    "1.2.4C"] = "1.2.4C Effective collaborative teams practice interpersonal communication, consensus building, conflict resolution, and negotiation.";
cspframework["1.2.4D"] = "1.2.4D Effective collaboration strategies enhance performance.";
cspframework[
    "1.2.4E"] = "1.2.4E Collaboration facilitates the application of multiple perspectives (including sociocultural perspectives) and diverse talents and skills in developing computational artifacts.";
cspframework[
    "1.2.4F"] = "1.2.4F A collaboratively created computational artifact can reflect personal expressions of ideas.";
cspframework[
    "1.2.5"] = "1.2.5 Analyze the correctness, usability, functionality, and suitability of computational artifacts. [P4]";
cspframework[
    "1.2.5A"] = "1.2.5A The context in which an artifact is used determines the correctness, usability, functionality, and suitability of the artifact.";
cspframework[
    "1.2.5B"] = "1.2.5B A computational artifact may have weaknesses, mistakes, or errors depending on the type of artifact.";
cspframework[
    "1.2.5C"] = "1.2.5C The functionality of a computational artifact may be related to how it is used or perceived.";
cspframework[
    "1.2.5D"] = "1.2.5D The suitability (or appropriateness) of a computational artifact may be related to how it is used or perceived.";
cspframework["1.3"] = "1.3 Computing can extend traditional forms of human expression and experience.";
cspframework["1.3.1"] = "1.3.1 Use computing tools and techniques for creative expression. [P2]";
cspframework[
    "1.3.1A"] = "1.3.1A Creating digital effects, images, audio, video, and animations has transformed industries.";
cspframework[
    "1.3.1B"] = "1.3.1B Digital audio and music can be created by synthesizing sounds, sampling existing audio and music, and recording and manipulating sounds, including layering and looping.";
cspframework[
    "1.3.1C"] = "1.3.1C Digital images can be created by generating pixel patterns, manipulating existing digital images, or combining images.";
cspframework[
    "1.3.1D"] = "1.3.1D Digital effects and animations can be created by using existing software or modified software that includes functionality to implement the effects and animations.";
cspframework["1.3.1E"] = "1.3.1E Computing enables creative exploration of both real and virtual phenomena.";
cspframework[
    "2.1"] = "2.1 A variety of abstractions built upon binary sequences can be used to represent all digital data.";
cspframework["2.1.1"] = "2.1.1 Describe the variety of abstractions used to represent data. [P3]";
cspframework["2.1.1A"] = "2.1.1A Digital data is represented by abstractions at different levels.";
cspframework["2.1.1B"] = "2.1.1B At the lowest level, all digital data are represented by bits.";
cspframework[
    "2.1.1C"] = "2.1.1C At a higher level, bits are grouped to represent abstractions, including but not limited to numbers, characters, and color.";
cspframework[
    "2.1.1D"] = "2.1.1D Number bases, including binary, decimal, and hexadecimal, are used to represent and investigate digital data.";
cspframework[
    "2.1.1E"] = "2.1.1E At one of the lowest levels of abstraction, digital data is represented in binary (base 2) using only combinations of the digits zero and one.";
cspframework[
    "2.1.1F"] = "2.1.1F Hexadecimal (base 16) is used to represent digital data because hexadecimal representation uses fewer digits than binary.";
cspframework["2.1.1G"] = "2.1.1G Numbers can be converted from any base to any other base.";
cspframework["2.1.2"] = "2.1.2 Explain how binary sequences are used to represent digital data. [P5]";
cspframework[
    "2.1.2A"] = "2.1.2A A finite representation is used to model the infinite mathematical concept of a number. ";
cspframework[
    "2.1.2B"] = "2.1.2B In many programming languages, the fixed number of bits used to represent characters or integers limits the range of integer values and mathematical operations; this limitation can result in overflow or other errors.";
cspframework[
    "2.3.1D"] = "2.3.1D Simulations mimic real world events without the cost or danger of building and testing the phenomena in the real world.";
cspframework[
    "2.1.2C"] = "2.1.2C In many programming languages, the fixed number of bits used to represent real numbers (as floating point numbers) limits the range of floating  point values and mathematical operations; this limitation can result in round";
cspframework[
    "2.2.3G"] = "2.2.3G A chip is an abstraction composed of low level components and circuits that perform a specific function.";
cspframework[
    "3.3.1A"] = "3.3.1A Digital data representations involve trade  offs related to storage, security, and privacy concerns.";
cspframework[
    "5.5.1C"] = "5.5.1C Real numbers are approximated by floating  point representations that do not necessarily have infinite precision.";
cspframework[
    "2.2.3K"] = "2.2.3K Lowerlevel abstractions can be combined to make higher level abstractions, such as short message services (SMS) or email messages, images, audio files, and videos.";
cspframework[
    "2.2.3C"] = "2.2.3C Code in a programming language is often translated into code in another (lowerlevel) language to be executed on a computer.";
cspframework["3.3.1B"] = "3.3.1B Security concerns engender tradeoffs in storing and transmitting information.";
cspframework[
    "3.3.1C"] = "3.3.1C There are trade offs in using lossy and lossless compression techniques for storing and transmitting data.";
cspframework["3.3"] = "3.3 There are trade offs when representing information as digital data.";
cspframework["6.3.1A"] = "6.3.1A The trust model of the Internet involves tradeoffs.";
cspframework[
    "7.1.2G"] = "7.1.2G The move from desktop computers to a proliferation of alwayson mobile computers is leading to new applications.";
cspframework[
    "5.3.1J"] = "5.3.1J Integers and floatingpoint numbers are used in programs without requiring understanding of how they are implemented.";
cspframework[
    "6.2.2F"] = "6.2.2F The Internet is a packetswitched system through which digital data is sent by breaking the data into blocks of bits called packets, which contain both the data being transmitted and control information for routing the data.";
cspframework[
    "6.1.1B"] = "6.1.1B An end to end architecture facilitates connecting new devices and networks on the Internet.";
cspframework[
    "7.3.1C"] = "7.3.1C Access to digital content via peer to peer networks raises legal and ethical concerns.";
cspframework["2.1.2D"] = "2.1.2D The interpretation of a binary sequence depends on how it is used.";
cspframework["2.1.2E"] = "2.1.2E A sequence of bits may represent instructions or data.";
cspframework["2.1.2F"] = "2.1.2F A sequence of bits may represent different types of data in different contexts.";
cspframework[
    "2.2"] = "2.2 Multiple levels of abstraction are used to write programs or create other computational artifacts";
cspframework[
    "2.2.1"] = "2.2.1 Develop an abstraction when writing a program or creating other computational artifacts. [P2]";
cspframework[
    "2.2.1A"] = "2.2.1A The process of developing an abstraction involves removing detail and generalizing functionality.";
cspframework[
    "2.2.1B"] = "2.2.1B An abstraction extracts common features from specific examples in order to generalize concepts.";
cspframework[
    "2.2.1C"] = "2.2.1C An abstraction generalizes functionality with input parameters that allow software reuse.";
cspframework["2.2.2"] = "2.2.2 Use multiple levels of abstraction to write programs. [P3]";
cspframework[
    "2.2.2A"] = "2.2.2A Software is developed using multiple levels of abstractions, such as constants, expressions, statements, procedures, and libraries.";
cspframework[
    "2.2.2B"] = "2.2.2B Being aware of and using multiple levels of abstraction in developing programs helps to more effectively apply available resources and tools to solve problems.";
cspframework["2.2.3"] = "2.2.3 Identify multiple levels of abstractions that are used when writing programs. [P3]";
cspframework["2.2.3A"] = "2.2.3A Different programming languages offer different levels of abstraction.";
cspframework[
    "2.2.3B"] = "2.2.3B High level programming languages provide more abstractions for the programmer and make it easier for people to read and write a program.";
cspframework[
    "2.2.3D"] = "2.2.3D In an abstraction hierarchy, higher levels of abstraction (the most general concepts) would be placed toward the top and lower level abstractions (the more specific concepts) toward the bottom.";
cspframework[
    "2.2.3E"] = "2.2.3E Binary data is processed by physical layers of computing hardware, including gates, chips, and components.";
cspframework["2.2.3F"] = "2.2.3F A logic gate is a hardware abstraction that is modeled by a Boolean function.";
cspframework[
    "2.2.3H"] = "2.2.3H A hardware component can be low level like a transistor or high level like a video card.";
cspframework[
    "2.2.3I"] = "2.2.3I Hardware is built using multiple levels of abstractions, such as transistors, logic gates, chips, memory, motherboards, special purposes cards, and storage devices.";
cspframework[
    "2.2.3J"] = "2.2.3J Applications and systems are designed, developed, and analyzed using levels of hardware, software, and conceptual abstractions.";
cspframework["2.3"] = "2.3 Models and simulations use abstraction to generate new understanding and knowledge.";
cspframework["2.3.1"] = "2.3.1 Use models and simulations to represent phenomena. [P3]";
cspframework[
    "2.3.1A"] = "2.3.1A Models and simulations are simplified representations of more complex objects or phenomena.";
cspframework[
    "2.3.1B"] = "2.3.1B Models may use different abstractions or levels of abstraction depending on the objects or phenomena being posed.";
cspframework[
    "2.3.1C"] = "2.3.1C Models often omit unnecessary features of the objects or phenomena that are being modeled.";
cspframework["2.3.2"] = "2.3.2 Use models and simulations to formulate, refine, and test hypotheses. [P3]";
cspframework[
    "2.3.2A"] = "2.3.2A Models and simulations facilitate the formulation and refinement of hypotheses related to the objects or phenomena under consideration.";
cspframework["2.3.2B"] = "2.3.2B Hypotheses are formulated to explain the objects or phenomena being modeled.";
cspframework[
    "2.3.2C"] = "2.3.2C Hypotheses are refined by examining the insights that models and simulations provide into the objects or phenomena.";
cspframework[
    "2.3.2D"] = "2.3.2D The results of simulations may generate new knowledge and new hypotheses related to the phenomena being modeled.";
cspframework["2.3.2E"] = "2.3.2E Simulations allow hypotheses to be tested without the constraints of the real world.";
cspframework["2.3.2F"] = "2.3.2F Simulations can facilitate extensive and rapid testing of models.";
cspframework[
    "2.3.2G"] = "2.3.2G The time required for simulations is impacted by the level of detail and quality of the models, and the software and hardware used for the simulation.";
cspframework[
    "2.3.2H"] = "2.3.2H Rapid and extensive testing allows models to be changed to accurately reflect the objects or phenomena being modeled.";
cspframework["3.1"] = "3.1 People use computer programs to process information to gain insight and knowledge.";
cspframework[
    "3.1.1"] = "3.1.1 Use computers to process information, find patterns, and test hypotheses about digitally processed information to gain insight and knowledge. [P4]";
cspframework[
    "3.1.1A"] = "3.1.1A Computers are used in an iterative and interactive way when processing digital information to gain insight and knowledge.";
cspframework[
    "3.1.1B"] = "3.1.1B Digital information can be filtered and cleaned by using computers to process information.";
cspframework[
    "3.1.1C"] = "3.1.1C Combining data sources, clustering data, and data classification are part of the process of using computers to process information.";
cspframework[
    "3.1.1D"] = "3.1.1D Insight and knowledge can be obtained from translating and transforming digitally represented information.";
cspframework["3.1.1E"] = "3.1.1E Patterns can emerge when data is transformed using computational tools.";
cspframework["3.1.2"] = "3.1.2 Collaborate when processing information to gain insight and knowledge. [P6]";
cspframework["3.1.2A"] = "3.1.2A Collaboration is an important part of solving data driven problems.";
cspframework[
    "3.1.2B"] = "3.1.2B Collaboration facilitates solving computational problems by applying multiple perspectives, experiences, and skill sets.";
cspframework[
    "3.1.2C"] = "3.1.2C Communication between participants working on data driven problems gives rise to enhanced insights and knowledge.";
cspframework[
    "3.1.2D"] = "3.1.2D Collaboration in developing hypotheses and questions, and in testing hypotheses and answering questions, about data helps participants gain insight and knowledge.";
cspframework[
    "3.1.2E"] = "3.1.2E Collaborating face-to-face and using online collaborative tools can facilitate processing information to gain insight and knowledge.";
cspframework[
    "3.1.2F"] = "3.1.2F Investigating large data sets collaboratively can lead to insight and knowledge not obtained when working alone.";
cspframework[
    "3.1.3"] = "3.1.3 Explain the insight and knowledge gained from digitally processed data by using appropriate visualizations, notations, and precise language. [P5]";
cspframework["3.1.3A"] = "3.1.3A Visualization tools and software can communicate information about data.";
cspframework[
    "3.1.3B"] = "3.1.3B Tables, diagrams, and textual displays can be used in communicating insight and knowledge gained from data.";
cspframework[
    "3.1.3C"] = "3.1.3C Summaries of data analyzed computationally can be effective in communicating insight and knowledge gained from digitally represented information.";
cspframework[
    "3.1.3D"] = "3.1.3D Transforming information can be effective in communicating knowledge gained from data.";
cspframework["3.1.3E"] = "3.1.3E Interactivity with data is an aspect of communicating.";
cspframework["3.2"] = "3.2 Computing facilitates exploration and the discovery of connections in information.";
cspframework[
    "3.2.1"] = "3.2.1 Extract information from data to discover and explain connections, patterns, or trends. [P1]";
cspframework[
    "3.2.1A"] = "3.2.1A Large data sets provide opportunities and challenges for extracting information and knowledge.";
cspframework[
    "3.2.1B"] = "3.2.1B Large data sets provide opportunities for identifying trends, making connections in data, and solving problems.";
cspframework[
    "3.2.1C"] = "3.2.1C Computing tools facilitate the discovery of connections in information within large data sets.";
cspframework["3.2.1D"] = "3.2.1D Search tools are essential for efficiently finding information.";
cspframework[
    "3.2.1E"] = "3.2.1E Information filtering systems are important tools for finding information and recognizing patterns in the information.";
cspframework[
    "3.2.1F"] = "3.2.1F Software tools, including spreadsheets and databases, help to efficiently organize and find trends in information.";
cspframework["3.2.1G"] = "3.2.1G Metadata is data about data.";
cspframework[
    "3.2.1H"] = "3.2.1H Metadata can be descriptive data about an image, a Web page, or other complex objects.";
cspframework[
    "3.2.1I"] = "3.2.1I Metadata can increase the effective use of data or data sets by providing additional information about various aspects of that data.";
cspframework["3.2.2"] = "3.2.2 Use large data sets to explore and discover information and knowledge. [P3]";
cspframework[
    "3.2.2A"] = "3.2.2A Large data sets include data such as transactions, measurements, text, sound, images, and video.";
cspframework["3.2.2B"] = "3.2.2B The storing, processing, and curating of large data sets is challenging.";
cspframework["3.2.2C"] = "3.2.2C Structuring large data sets for analysis can be challenging.";
cspframework[
    "3.2.2D"] = "3.2.2D Maintaining privacy of large data sets containing personal information can be challenging.";
cspframework["3.2.2E"] = "3.2.2E Scalability of systems is an important consideration when data sets are large.";
cspframework["3.2.2F"] = "3.2.2F The size or scale of a system that stores data affects how that data set is used.";
cspframework["3.2.2G"] = "3.2.2G The effective use of large data sets requires computational solutions.";
cspframework[
    "3.2.2H"] = "3.2.2H Analytical techniques to store, manage, transmit, and process data sets change as the size of data sets scale.";
cspframework[
    "3.3.1"] = "3.3.1 Analyze how data representation, storage, security, and transmission of data involve computational manipulation of information. [P4]";
cspframework[
    "3.3.1D"] = "3.3.1D Lossless data compression reduces the number of bits stored or transmitted but allows complete reconstruction of the original data";
cspframework[
    "3.3.1E"] = "3.3.1E Lossy data compression can significantly reduce the number of bits stored or transmitted at the cost of being able to reconstruct only an approximation of the original data.";
cspframework["3.3.1F"] = "3.3.1F Security and privacy concerns arise with data containing personal information.";
cspframework[
    "3.3.1G"] = "3.3.1G Data is stored in many formats depending on its characteristics (e.g., size and intended use)";
cspframework[
    "3.3.1H"] = "3.3.1H The choice of storage media affects both the methods and costs of manipulating the data it contains.";
cspframework["3.3.1I"] = "3.3.1I Reading data and updating data have different storage requirements.";
cspframework[
    "4.1"] = "4.1 Algorithms are precise sequences of instructions for processes that can be executed by a computer and are implemented using programming languages.";
cspframework["4.1.1"] = "4.1.1 Develop an algorithm for implementation in a program. [P2]";
cspframework["4.1.1A"] = "4.1.1A Sequencing, selection, and iteration are building blocks of algorithms.";
cspframework[
    "4.1.1B"] = "4.1.1B Sequencing is the application of each step of an algorithm in the order in which the statements are given.";
cspframework[
    "4.1.1C"] = "4.1.1C Selection uses a Boolean condition to determine which of two parts of an algorithm is used.";
cspframework[
    "4.1.1D"] = "4.1.1D Iteration is the repetition of part of an algorithm until a condition is met or for a specified number of times.";
cspframework["4.1.1E"] = "4.1.1E Algorithms can be combined to make new algorithms.";
cspframework[
    "4.1.1F"] = "4.1.1F Using existing correct algorithms as building blocks for constructing a new algorithm helps ensure the new algorithm is correct.";
cspframework["4.1.1G"] = "4.1.1G Knowledge of standard algorithms can help in constructing new algorithms.";
cspframework["4.1.1H"] = "4.1.1H Different algorithms can be developed to solve the same problem.";
cspframework["4.1.1I"] = "4.1.1I Developing a new algorithm to solve a problem can yield insight into the problem.";
cspframework["4.1.2"] = "4.1.2 Express an algorithm in a language. [P5]";
cspframework[
    "4.1.2A"] = "4.1.2A Languages for algorithms include natural language, pseudocode, and visual and textual programming languages.";
cspframework[
    "4.1.2B"] = "4.1.2B Natural language and pseudocode describe algorithms so that humans can understand them.";
cspframework["4.1.2C"] = "4.1.2C Algorithms described in programming languages can be executed on a computer.";
cspframework["4.1.2D"] = "4.1.2D Different languages are better suited for expressing different algorithms.";
cspframework[
    "4.1.2E"] = "4.1.2E Some programming languages are designed for specific domains and are better for expressing algorithms in those domains.";
cspframework[
    "4.1.2F"] = "4.1.2F The language used to express an algorithm can affect characteristics such as clarity or readability but not whether an algorithmic solution exists.";
cspframework["4.1.2G"] = "4.1.2G Every algorithm can be constructed using only sequencing, selection, and iteration.";
cspframework[
    "4.1.2H"] = "4.1.2H Nearly all programming languages are equivalent in terms of being able to express any algorithm.";
cspframework[
    "4.1.2I"] = "4.1.2I Clarity and readability are important considerations when expressing an algorithm in a language.";
cspframework["4.2"] = "4.2 Algorithms can solve many but not all computational problems.";
cspframework[
    "4.2.1"] = "4.2.1 Explain the difference between algorithms that run in a reasonable time and those that do not run in a reasonable time. [P1]";
cspframework["4.2.1A"] = "4.2.1A Many problems can be solved in a reasonable time.";
cspframework[
    "4.2.1B"] = "4.2.1B Reasonable time means that as the input size grows, the number of steps the algorithm takes is proportional to the square (or cube, fourth power, fifth power, etc.) of the size of the input. ";
cspframework["4.2.1C"] = "4.2.1C Some problems cannot be solved in a reasonable time, even for small input sizes.";
cspframework[
    "4.2.1D"] = "4.2.1D Some problems can be solved but not in a reasonable time. In these cases, heuristic approaches may be helpful to find solutions in reasonable time.";
cspframework[
    "4.2.2"] = "4.2.2 Explain the difference between solvable and unsolvable problems in computer science. [P1]";
cspframework[
    "4.2.2A"] = "4.2.2A A heuristic is a technique that may allow us to find an approximate solution when typical methods fail to find an exact solution.";
cspframework[
    "4.2.2B"] = "4.2.2B Heuristics may be helpful for finding an approximate solution more quickly when exact methods are too slow.";
cspframework[
    "4.2.2C"] = "4.2.2C Some optimization problems such as â€œfind the bestâ€ or â€œfind the smallestâ€ cannot be solved in a reasonable time, but approximations to the optimal solution can.";
cspframework["4.2.2D"] = "4.2.2D Some problems cannot be solved using any algorithm.";
cspframework["4.2.3"] = "4.2.3 Explain the existence of undecidable problems in computer science. [P1]";
cspframework[
    "4.2.3A"] = "4.2.3A An undecidable problem may have instances that have an algorithmic solution, but there is no algorithmic solution that solves all instances of the problem.";
cspframework[
    "4.2.3B"] = "4.2.3B A decidable problem is one in which an algorithm can be constructed to answer â€œyesâ€ or â€œnoâ€ for all inputs (e.g., â€œis the number even?â€)";
cspframework[
    "4.2.3C"] = "4.2.3C An undecidable problem is one in which no algorithm can be constructed that always leads to a correct yes or no answer";
cspframework[
    "4.2.4"] = "4.2.4 Evaluate algorithms analytically and empirically for efficiency, correctness, and clarity. [P4]";
cspframework[
    "4.2.4A"] = "4.2.4A Determining an algorithmâ€™s efficiency is done by reasoning formally or mathematically about the algorithm.";
cspframework[
    "4.2.4B"] = "4.2.4B Empirical analysis of an algorithm is done by implementing the algorithm and running it on different inputs.";
cspframework[
    "4.2.4C"] = "4.2.4C The correctness of an algorithm is determined by reasoning formally or mathematically about the algorithm, not by testing an implementation of the algorithm.";
cspframework["4.2.4D"] = "4.2.4D Different correct algorithms for the same problem can have different efficiencies.";
cspframework["4.2.4E"] = "4.2.4E Sometimes more efficient algorithms are more complex.";
cspframework[
    "4.2.4F"] = "4.2.4F Finding an efficient algorithm for a problem can help solve larger instances of the problem.";
cspframework["4.2.4G"] = "4.2.4G Efficiency includes both execution time and memory usage.";
cspframework[
    "4.2.4H"] = "4.2.4H Linear search can be used when searching for an item in any list; binary search can be used only when the list is sorted.";
cspframework[
    "5.1"] = "5.1 Programs can be developed for creative expression, to satisfy personal curiosity, to create new knowledge, or to solve problems (to help people, organizations, or society).";
cspframework[
    "5.1.1"] = "5.1.1 Develop a program for creative expression, to satisfy personal curiosity, or to create new knowledge. [P2]";
cspframework[
    "5.1.1A"] = "5.1.1A Programs are developed and used in a variety of ways by a wide range of people depending on the goals of the programmer.";
cspframework[
    "5.1.1B"] = "5.1.1B Programs developed for creative expression, to satisfy personal curiosity, or to create new knowledge may have visual, audible, or tactile inputs and outputs.";
cspframework[
    "5.1.1C"] = "5.1.1C Programs developed for creative expression, to satisfy personal curiosity, or to create new knowledge may be developed with different standards or methods than programs developed for widespread distribution.";
cspframework[
    "5.1.1D"] = "5.1.1D Additional desired outcomes may be realized independently of the original purpose of the program.";
cspframework[
    "5.1.1E"] = "5.1.1E A computer program or the results of running a program may be rapidly shared with a large number of users and can have widespread impact on individuals, organizations, and society";
cspframework["5.1.1F"] = "5.1.1F Advances in computing have generated and increased creativity in other fields.";
cspframework["5.1.2"] = "5.1.2 Develop a correct program to solve problems. [P2]";
cspframework[
    "5.1.2A"] = "5.1.2A An iterative process of program development helps in developing a correct program to solve problems.";
cspframework[
    "5.1.2B"] = "5.1.2B Developing correct program components and then combining them helps in creating correct programs.";
cspframework[
    "5.1.2C"] = "5.1.2C Incrementally adding tested program segments to correct, working programs helps create large correct programs.";
cspframework[
    "5.1.2D"] = "5.1.2D Program documentation helps programmers develop and maintain correct programs to efficiently solve problems.";
cspframework[
    "5.1.2E"] = "5.1.2E Documentation about program components, such as blocks and procedures, helps in developing and maintaining programs.";
cspframework[
    "5.1.2F"] = "5.1.2F Documentation helps in developing and maintaining programs when working individually or in collaborative programming environments";
cspframework[
    "5.1.2G"] = "5.1.2G Program development includes identifying programmer and user concerns that affect the solution to problems.";
cspframework[
    "5.1.2H"] = "5.1.2H Consultation and communication with program users is an important aspect of program development to solve problems.";
cspframework[
    "5.1.2I"] = "5.1.2I A programmerâ€™s knowledge and skill affects how a program is developed and how it is used to solve a problem.";
cspframework[
    "5.1.2J"] = "5.1.2J A programmer designs, implements, tests, debugs, and maintains programs when solving problems.";
cspframework["5.1.3"] = "5.1.3 Collaborate to develop a program. [P6]";
cspframework[
    "5.1.3A"] = "5.1.3A Collaboration can decrease the size and complexity of tasks required of individual programmers.";
cspframework[
    "5.1.3B"] = "5.1.3B Collaboration facilitates multiple perspectives in developing ideas for solving problems by programming.";
cspframework[
    "5.1.3C"] = "5.1.3C Collaboration in the iterative development of a program requires different skills than developing a program alone.";
cspframework["5.1.3D"] = "5.1.3D Collaboration can make it easier to find and correct errors when developing programs.";
cspframework["5.1.3E"] = "5.1.3E Collaboration facilitates developing program components independently.";
cspframework[
    "5.1.3F"] = "5.1.3F Effective communication between participants is required for successful collaboration when developing programs.";
cspframework["5.2"] = "5.2 People write programs to execute algorithms.";
cspframework["5.2.1"] = "5.2.1 Explain how programs implement algorithms. [P3]";
cspframework[
    "5.2.1A"] = "5.2.1A Algorithms are implemented using program instructions that are processed during program execution.";
cspframework["5.2.1B"] = "5.2.1B Program instructions are executed sequentially.";
cspframework[
    "5.2.1C"] = "5.2.1C Program instructions may involve variables that are initialized and updated, read, and written";
cspframework[
    "5.2.1D"] = "5.2.1D An understanding of instruction processing and program execution is useful for programming.";
cspframework["5.2.1E"] = "5.2.1E Program execution automates processes.";
cspframework["5.2.1F"] = "5.2.1F Processes use memory, a central processing unit (CPU), and input and output.";
cspframework["5.2.1G"] = "5.2.1G A process may execute by itself or with other processes.";
cspframework["5.2.1H"] = "5.2.1H A process may execute on one or several CPUs.";
cspframework["5.2.1I"] = "5.2.1I Executable programs increase the scale of problems that can be addressed.";
cspframework["5.2.1J"] = "5.2.1J Simple algorithms can solve a large set of problems when automated.";
cspframework[
    "5.2.1K"] = "5.2.1K Improvements in algorithms, hardware, and software increase the kinds of problems and the size of problems solvable by programming.";
cspframework["5.3"] = "5.3 Programming is facilitated by appropriate abstractions.";
cspframework["5.3.1"] = "5.3.1 Use abstraction to manage complexity in programs. [P3]";
cspframework["5.3.1A"] = "5.3.1A Procedures are reusable programming abstractions.";
cspframework["5.3.1B"] = "5.3.1B A function is a named grouping of programming instructions.";
cspframework["5.3.1C"] = "5.3.1C Procedures reduce the complexity of writing and maintaining programs.";
cspframework["5.3.1D"] = "5.3.1D Procedures have names and may have parameters and return values.";
cspframework["5.3.1E"] = "5.3.1E Parameterization can generalize a specific solution.";
cspframework[
    "5.3.1F"] = "5.3.1F Parameters generalize a solution by allowing a function to be used instead of duplicated code";
cspframework[
    "5.3.1G"] = "5.3.1G Parameters provide different values as input to procedures when they are called in a program.";
cspframework["5.3.1H"] = "5.3.1H Data abstraction provides a means of separating behavior from implementation.";
cspframework[
    "5.3.1I"] = "5.3.1I Strings and string operations, including concatenation and some form of substring, are common in many programs.";
cspframework[
    "5.3.1K"] = "5.3.1K Lists and list operations, such as add, remove, and search, are common in many programs.";
cspframework[
    "5.3.1L"] = "5.3.1L Using lists and procedures as abstractions in programming can result in programs that are easier to develop and maintain.";
cspframework[
    "5.3.1M"] = "5.3.1M Application program interfaces (APIs) and libraries simplify complex programming tasks.";
cspframework["5.3.1N"] = "5.3.1N Documentation for an API/library is an important aspect of programming.";
cspframework["5.3.1O"] = "5.3.1O APIs connect software components, allowing them to communicate.";
cspframework["5.4"] = "5.4 Programs are developed, maintained, and used by people for different purposes.";
cspframework["5.4.1"] = "5.4.1 Evaluate the correctness of a program. [P4]";
cspframework["5.4.1A"] = "5.4.1A Program style can affect the determination of program correctness.";
cspframework["5.4.1B"] = "5.4.1B Duplicated code can make it harder to reason about a program.";
cspframework["5.4.1C"] = "5.4.1C Meaningful names for variables and procedures help people better understand programs.";
cspframework["5.4.1D"] = "5.4.1D Longer code blocks are harder to reason about than shorter code blocks in a program.";
cspframework["5.4.1E"] = "5.4.1E Locating and correcting errors in a program is called debugging the program.";
cspframework[
    "5.4.1F"] = "5.4.1F Knowledge of what a program is supposed to do is required in order to find most program errors.";
cspframework[
    "5.4.1G"] = "5.4.1G Examples of intended behavior on specific inputs help people understand what a program is supposed to do.";
cspframework[
    "5.4.1H"] = "5.4.1H Visual displays (or different modalities) of program state can help in finding errors.";
cspframework["5.4.1I"] = "5.4.1I Programmers justify and explain a programâ€™s correctness.";
cspframework[
    "5.4.1J"] = "5.4.1J Justification can include a written explanation about how a program meets its specifications.";
cspframework[
    "5.4.1K"] = "5.4.1K Correctness of a program depends on correctness of program components, including code blocks and procedures.";
cspframework[
    "5.4.1L"] = "5.4.1L An explanation of a program helps people understand the functionality and purpose of it.";
cspframework["5.4.1M"] = "5.4.1M The functionality of a program is often described by how a user interacts with it.";
cspframework[
    "5.4.1N"] = "5.4.1N The functionality of a program is best described at a high level by what the program does, not at the lower level of how the program statements work to accomplish this.";
cspframework["5.5"] = "5.5 Programming uses mathematical and logical concepts.";
cspframework["5.5.1"] = "5.5.1 Employ appropriate mathematical and logical concepts in programming. [P1]";
cspframework["5.5.1A"] = "5.5.1A Numbers and numerical concepts are fundamental to programming.";
cspframework[
    "5.5.1B"] = "5.5.1B Integers may be constrained in the maximum and minimum values that can be represented in a program because of storage limitations.";
cspframework[
    "5.5.1D"] = "5.5.1D Mathematical expressions using arithmetic operators are part of most programming languages.";
cspframework["5.5.1E"] = "5.5.1E Logical concepts and Boolean algebra are fundamental to programming.";
cspframework["5.5.1F"] = "5.5.1F Compound expressions using and, or, and not are part of most programming languages. ";
cspframework[
    "5.5.1G"] = "5.5.1G Intuitive and formal reasoning about program components using Boolean concepts helps in developing correct programs.";
cspframework["5.5.1H"] = "5.5.1H Computational methods may use lists and collections to solve problems.";
cspframework[
    "5.5.1I"] = "5.5.1I Lists and other collections can be treated as abstract data types (ADTs) in developing programs.";
cspframework[
    "5.5.1J"] = "5.5.1J Basic operations on collections include adding elements, removing elements, iterating over all elements, and determining whether an element is in a collection.";
cspframework["6.1"] = "6.1 The Internet is a network of autonomous systems.";
cspframework["6.1.1"] = "6.1.1 Explain the abstractions in the Internet and how the Internet functions. [P3]";
cspframework["6.1.1A"] = "6.1.1A The Internet connects devices and networks all over the world.";
cspframework[
    "6.1.1C"] = "6.1.1C Devices and networks that make up the Internet are connected and communicate using addresses and protocols.";
cspframework["6.1.1D"] = "6.1.1D The Internet and the systems built on it facilitate collaboration.";
cspframework[
    "6.1.1E"] = "6.1.1E Connecting new devices to the Internet is enabled by assignment of an Internet protocol (IP) address.";
cspframework["6.1.1F"] = "6.1.1F The Internet is built on evolving standards, including those for addresses and names.";
cspframework["6.1.1G"] = "6.1.1G The domain name system (DNS) translates names to IP addresses.";
cspframework[
    "6.1.1H"] = "6.1.1H The number of devices that could use an IP address has grown so fast that a new protocol (IPv6) has been established to handle routing of many more devices.";
cspframework[
    "6.1.1I"] = "6.1.1I Standards such as hypertext transfer protocol (HTTP), IP, and simple mail transfer protocol (SMTP) are developed and overseen by the Internet Engineering Task Force (IETF).";
cspframework["6.2"] = "6.2 Characteristics of the Internet influence the systems built on it.";
cspframework["6.2.1"] = "6.2.1 Explain characteristics of the Internet and the systems built on it. [P5]";
cspframework["6.2.1A"] = "6.2.1A The Internet and the systems built on it are hierarchical and redundant.";
cspframework["6.2.1B"] = "6.2.1B The domain name syntax is hierarchical";
cspframework["6.2.1C"] = "6.2.1C IP addresses are hierarchical.";
cspframework["6.2.1D"] = "6.2.1D Routing on the Internet is fault tolerant and redundant.";
cspframework["6.2.2"] = "6.2.2 Explain how the characteristics of the Internet influence the systems built on it. [P4]";
cspframework["6.2.2A"] = "6.2.2A Hierarchy and redundancy help systems scale.";
cspframework[
    "6.2.2B"] = "6.2.2B The redundancy of routing (i.e., more than one way to route data) between two points on the Internet increases the reliability of the Internet and helps it scale to more devices and more people.";
cspframework["6.2.2C"] = "6.2.2C Hierarchy in the DNS helps that system scale.";
cspframework["6.2.2D"] = "6.2.2D Interfaces and protocols enable widespread use of the Internet.";
cspframework["6.2.2E"] = "6.2.2E Open standards fuel the growth of the Internet.";
cspframework[
    "6.2.2F"] = "6.2.2F The Internet is a packet-switched system through which digital data is sent by breaking the data into blocks of bits called packets, which contain both the data being transmitted and control information for routing the data.";
cspframework[
    "6.2.2G"] = "6.2.2G Standards for packets and routing include transmission control protocol/Internet protocol (TCP/IP).";
cspframework[
    "6.2.2H"] = "6.2.2H Standards for sharing information and communicating between browsers and servers on the Web include HTTP and secure sockets layer/transport layer security (SSL/TLS).";
cspframework["6.2.2I"] = "6.2.2I The size and speed of systems affect their use.";
cspframework[
    "6.2.2J"] = "6.2.2J The bandwidth of a system is a measure of bit rate â€” the amount of data (measured in bits) that can be sent in a fixed amount of time.";
cspframework[
    "6.2.2K"] = "6.2.2K The latency of a system is the time elapsed between the transmission and the receipt of a request.";
cspframework["6.3"] = "6.3 Cybersecurity is an important concern for the Internet and the systems built on it.";
cspframework[
    "6.3.1"] = "6.3.1 Identify existing cybersecurity concerns and potential options to address these issues with the Internet and the systems built on it. [P1]";
cspframework["6.3.1B"] = "6.3.1B The domain name system (DNS) was not designed to be completely secure.";
cspframework["6.3.1C"] = "6.3.1C Implementing cybersecurity has software, hardware, and human components.";
cspframework["6.3.1D"] = "6.3.1D Cyber warfare and cyber crime have widespread and potentially devastating effects.";
cspframework[
    "6.3.1E"] = "6.3.1E Distributed denial of service attacks (DDoS) compromise a target by flooding it with requests from multiple systems.";
cspframework["6.3.1F"] = "6.3.1F Phishing, viruses, and other attacks have human and software components.";
cspframework[
    "6.3.1G"] = "6.3.1G Antivirus software and firewalls can help prevent unauthorized access to private data.";
cspframework["6.3.1H"] = "6.3.1H Cryptography is essential to many models of cybersecurity.";
cspframework["6.3.1I"] = "6.3.1I Cryptography has a mathematical foundation.";
cspframework["6.3.1J"] = "6.3.1J Open standards help ensure cryptography is secure.";
cspframework[
    "6.3.1K"] = "6.3.1K Symmetric encryption is a method of encryption involving one key for encryption and decryption.";
cspframework[
    "6.3.1L"] = "6.3.1L Public key encryption, which is not symmetric, is an encryption method that is widely used because of the enhanced security associated with its use.";
cspframework[
    "6.3.1M"] = "6.3.1M Certificate authorities (CAs) issue digital certificates that validate the ownership of encrypted keys used in secured communication and are based on a trust model.";
cspframework["7.1"] = "7.1 Computing enhances communication, interaction, and cognition.";
cspframework[
    "7.1.1"] = "7.1.1 Explain how computing innovations affect communication, interaction, and cognition. [P4]";
cspframework[
    "7.1.1A"] = "7.1.1A Email, short message service (SMS), and chat have fostered new ways to communicate and collaborate.";
cspframework[
    "7.1.1B"] = "7.1.1B Video conferencing and video chat have fostered new ways to communicate and collaborate.";
cspframework["7.1.1C"] = "7.1.1C Social media continues to evolve and foster new ways to communicate.";
cspframework["7.1.1D"] = "7.1.1D Cloud computing fosters new ways to communicate and collaborate.";
cspframework[
    "7.1.1E"] = "7.1.1E Widespread access to information facilitates the identification of problems, development of solutions, and dissemination of results.";
cspframework["7.1.1F"] = "7.1.1F Public data provides widespread access and enables solutions to identified problems.";
cspframework["7.1.1G"] = "7.1.1G Search trends are predictors.";
cspframework["7.1.1H"] = "7.1.1H Social media, such as blogs and Twitter, have enhanced dissemination.";
cspframework[
    "7.1.1I"] = "7.1.1I Global Positioning System (GPS) and related technologies have changed how humans travel, navigate, and find information related to geolocation.";
cspframework[
    "7.1.1J"] = "7.1.1J Sensor networks facilitate new ways of interacting with the environment and with physical systems.";
cspframework[
    "7.1.1K"] = "7.1.1K Smart grids, smart buildings, and smart transportation are changing and facilitating human capabilities.";
cspframework["7.1.1L"] = "7.1.1L Computing contributes to many assistive technologies that enhance human capabilities.";
cspframework[
    "7.1.1M"] = "7.1.1M The Internet and the Web have enhanced methods of and opportunities for communication and collaboration.";
cspframework[
    "7.1.1N"] = "7.1.1N The Internet and the Web have changed many areas, including ecommerce, health care, access to information and entertainment, and online learning.";
cspframework[
    "7.1.1O"] = "7.1.1O The Internet and the Web have impacted productivity, positively and negatively, in many areas.";
cspframework["7.1.2"] = "7.1.2 Explain how people participate in a problem solving process that scales. [P4]";
cspframework["7.1.2A"] = "7.1.2A Distributed solutions must scale to solve some problems.";
cspframework[
    "7.1.2B"] = "7.1.2B Science has been impacted by using scale and â€œcitizen scienceâ€ to solve scientific problems using home computers in scientific research.";
cspframework[
    "7.1.2C"] = "7.1.2C Human computation harnesses contributions from many humans to solve problems related to digital data and the Web.";
cspframework["7.1.2D"] = "7.1.2D Human capabilities are enhanced by digitally enabled collaboration.";
cspframework[
    "7.1.2E"] = "7.1.2E Some online services use the contributions of many people to benefit both individuals and society.";
cspframework[
    "7.1.2F"] = "7.1.2F Crowdsourcing offers new models for collaboration, such as connecting people with jobs and businesses with funding.";
cspframework["7.2"] = "7.2 Computing enables innovation in nearly every field.";
cspframework["7.2.1"] = "7.2.1 Explain how computing has impacted innovations in other fields. [P1]";
cspframework[
    "7.2.1A"] = "7.2.1A Machine learning and data mining have enabled innovation in medicine, business, and science.";
cspframework["7.2.1B"] = "7.2.1B Scientific computing has enabled innovation in science and business.";
cspframework["7.2.1C"] = "7.2.1C Computing enables innovation by providing access to and sharing of information.";
cspframework["7.2.1D"] = "7.2.1D Open access and Creative Commons have enabled broad access to digital information.";
cspframework["7.2.1E"] = "7.2.1E Open and curated scientific databases have benefited scientific researchers.";
cspframework[
    "7.2.1F"] = "7.2.1F Mooreâ€™s law has encouraged industries that use computers to effectively plan future research and development based on anticipated increases in computing power.";
cspframework[
    "7.2.1G"] = "7.2.1G Advances in computing as an enabling technology have generated and increased the creativity in other fields.";
cspframework["7.3"] = "7.3 Computing has a global affect â€” both beneficial and harmful â€” on people and society.";
cspframework["7.3.1"] = "7.3.1 Analyze the beneficial and harmful effects of computing. [P4]";
cspframework["7.3.1A"] = "7.3.1A Innovations enabled by computing raise legal and ethical concerns.";
cspframework[
    "7.3.1B"] = "7.3.1B Commercial access to music and movie downloads and streaming raises legal and ethical concerns.";
cspframework[
    "7.3.1D"] = "7.3.1D Both authenticated and anonymous access to digital information raise legal and ethical concerns.";
cspframework[
    "7.3.1E"] = "7.3.1E Commercial and governmental censorship of digital information raise legal and ethical concerns.";
cspframework["7.3.1F"] = "7.3.1F Open source and licensing of software and content raise legal and ethical concerns.";
cspframework[
    "7.3.1G"] = "7.3.1G Privacy and security concerns arise in the development and use of computational systems and artifacts.";
cspframework[
    "7.3.1H"] = "7.3.1H Aggregation of information, such as geolocation, cookies, and browsing history, raises privacy and security concerns.";
cspframework[
    "7.3.1I"] = "7.3.1I Anonymity in online interactions can be enabled through the use of online anonymity software and proxy servers.";
cspframework[
    "7.3.1J"] = "7.3.1J Technology enables the collection, use, and exploitation of information about, by, and for individuals, groups, and institutions.";
cspframework[
    "7.3.1K"] = "7.3.1K People can have instant access to vast amounts of information online; accessing this information can enable the collection of both individual and aggregate data that can be used and collected.";
cspframework[
    "7.3.1L"] = "7.3.1L Commercial and governmental curation of information may be exploited if privacy and other protections are ignored.";
cspframework[
    "7.3.1M"] = "7.3.1M Targeted advertising is used to help individuals, but it can be misused at both individual and aggregate levels.";
cspframework[
    "7.3.1N"] = "7.3.1N Widespread access to digitized information raises questions about intellectual property.";
cspframework[
    "7.3.1O"] = "7.3.1O Creation of digital audio, video, and textual content by combining existing content has been impacted by copyright concerns.";
cspframework[
    "7.3.1P"] = "7.3.1P The Digital Millennium Copyright Act (DMCA) has been a benefit and a challenge in making copyrighted digital material widely available.";
cspframework[
    "7.3.1Q"] = "7.3.1Q Open source and free software have practical, business, and ethical impacts on widespread access to programs, libraries, and code.";
cspframework[
    "7.4"] = "7.4 Computing innovations influence and are influenced by the economic, social, and cultural contexts in which they are designed and used.";
cspframework[
    "7.4.1"] = "7.4.1 Explain the connections between computing and economic, social, and cultural contexts. [P1]";
cspframework[
    "7.4.1A"] = "7.4.1A The innovation and impact of social media and online access is different in different countries and in different socioeconomic groups.";
cspframework[
    "7.4.1B"] = "7.4.1B Mobile, wireless, and networked computing have an impact on innovation throughout the world.";
cspframework[
    "7.4.1C"] = "7.4.1C The global distribution of computing resources raises issues of equity, access, and power.";
cspframework[
    "7.4.1D"] = "7.4.1D Groups and individuals are affected by the â€œdigital divideâ€ â€” differing access to computing and the Internet based on socioeconomic or geographic characteristics.";
cspframework[
    "7.4.1E"] = "7.4.1E Networks and infrastructure are supported by both commercial and governmental initiatives.";
cspframework[
    "2.1.1E.Ex"] = "<mark>Exclusion Statement</mark> (2.1.1E):</mark> Two's complement conversions are beyond the scope of this course and the AP Exam."
cspframework[
    "2.1.2B.Ex"] = "<mark>Exclusion Statement</mark> (2.1.2B): Range limitations of any one language, compiler, or architecture are beyond the scope of this course and the AP Exam.";
cspframework[
    "2.2.1C.Ex"] = "<mark>Exclusion Statement:</mark> (2.2.1C): An understanding of the difference between value and reference parameters is beyond the scope of this course and the AP Exam.";
cspframework[
    "2.2.3A.Ex"] = "<mark>Exclusion Statement</mark> (2.2.3A): Knowledge of the abstraction capabilities of all programming languages is beyond the scope of this course and the AP Exam.";
cspframework[
    "2.2.3F.Ex"] = "<mark>Exclusion Statement</mark> (2.2.3F): Memorization of specific gate visual representations is beyond the scope of this course and the AP Exam.";
cspframework[
    "3.2.1F.Ex"] = "<mark>Exclusion Statement</mark> (3.2.1F): Students are not expected to know specific formulas or options available in spreadsheet or database software packages..";
cspframework[
    "4.2.1.Ex"] = "<mark>Exclusion Statement</mark> (LO 4.2.1): Any discussion of nondeterministic polynomial (NP) is beyond the scope of this course and the AP Exam.";
cspframework[
    "4.2.2.Ex"] = "<mark>Exclusion Statement</mark> (LO 4.2.2): Determining whether a given problem is olvable or unsolvable is beyond the scope of this course and the AP Exam.";
cspframework[
    "4.2.2B.Ex"] = "<mark>Exclusion Statement</mark> (4.2.2B): Specific heuristic solutions are beyond the scope of this course and the AP Exam.";
cspframework[
    "4.2.3C.Ex"] = "<mark>Exclusion Statement</mark> (4.2.3C): Determining whether a given problem is undecidable is beyond the scope of this course and the AP Exam.";
cspframework[
    "4.2.4C.Ex"] = "<mark>Exclusion Statement</mark> (4.2.4C): Formally proving program correctness is beyond the scope of this course and the AP Exam.";
cspframework[
    "4.2.4G.Ex"] = "<mark>Exclusion Statement</mark> (4.2.4G): Formal analysis of algorithms (BigO) and formal reasoning using mathematical formulas are beyond the scope of this course and the AP Exam.";
cspframework[
    "5.5.1B.Ex"] = "<mark>Exclusion Statement</mark> (5.5.1B): Specific range limitations of all programming languages are beyond the scope of this course and the AP Exam.";
cspframework[
    "5.5.1C.Ex"] = "<mark>Exclusion Statement</mark> (5.5.1C): Specific sets of values that cannot be exactly represented by floating point numbers are beyond the scope of this course and the AP Exam.";
cspframework[
    "6.1.1.Ex"] = "<mark>Exclusion Statement</mark> (LO 6.1.1): Specific devices used to implement the abstractions in the Internet are beyond the scope of this course and the AP Exam.";
cspframework[
    "6.1.1F.Ex"] = "<mark>Exclusion Statement</mark> (6.1.1F): Specific details of any particular standard for addresses are beyond the scope of this course and the AP Exam.";
cspframework[
    "6.2.2F.Ex"] = "<mark>Exclusion Statement</mark> (6.2.2F): Specific details of any particular packet  switching system are beyond the scope of this course and the AP Exam.";
cspframework[
    "6.2.2G.Ex"] = "<mark>Exclusion Statement</mark> (6.2.2G): Specific technical details of how TCP/IP works are beyond the scope of this course and the AP Exam.";
cspframework[
    "6.2.2H.Ex"] = "<mark>Exclusion Statement</mark> (6.2.2H): Understanding the technical aspects of how SSL/TLS works is beyond the scope of this course and the AP Exam.";
cspframework[
    "6.3.1I.Ex"] = "<mark>Exclusion Statement</mark> (6.3.1I): Specific mathematical functions used in cryptography are beyond the scope of this course and the AP Exam.";
cspframework[
    "6.3.1K.Ex"] = "<mark>Exclusion Statement</mark> (6.3.1K): The methods used in encryption are beyond the scope of this course and the AP Exam.";
cspframework[
    "6.3.1L.Ex"] = "<mark>Exclusion Statement</mark> (6.3.1L): The mathematical methods used in public key encryption are beyond the scope of this course and the AP Exam.";
cspframework[
    "6.3.1M.Ex"] = "<mark>Exclusion Statement</mark> (6.3.1M): The technical details of the process certificate authorities follow are beyond the scope of this course and the AP Exam.";
cspframework[
    "7.1.1C.Ex"] = "<mark>Exclusion Statement</mark> (7.1.1C): Detailed knowledge of any social media site is beyond the scope of this course and the AP Exam.";

eus = {}
los = {}
eks = {}

# Sort into eus, los, and eks based on shortcode
for k, v in cspframework.iteritems():
    v = re.sub('\A[1-9]\.[1-9]\S*\s', '', v)
    eumatch = re.match('\A[1-9]\.[1-9]$', k)
    lomatch = re.match('\A[1-9]\.[1-9]\.[1-9]$', k)
    ekmatch = re.match('\A[1-9]\.[1-9]\.[1-9][A-Z]$', k)
    if eumatch: eus[k] = v
    if lomatch: los[k] = v
    if ekmatch: eks[k] = v

# import eus as top level categories
for k, v in eus.iteritems():
    eu = Category.objects.get_or_create(framework=framework, name=v, description=v, shortcode=k, type='EU')
    print eu

# import los as second level categories, under the appropriate eu
for k, v in los.iteritems():
    eu = Category.objects.get(framework=framework, shortcode=re.match('\A[1-9].[1-9]', k).group(0))
    lo = Category.objects.get_or_create(framework=framework, name=v, description=v, shortcode=k, type='LO', parent=eu)
    print lo

# import eks as standards under the appropriate lo
for k, v in eks.iteritems():
    gradeband = GradeBand.objects.get(name='9-12')
    lo = Category.objects.get(framework=framework, shortcode=re.match('\A[1-9].[1-9].[1-9]', k).group(0))
    ek = Standard.objects.get_or_create(framework=framework, name=v, description=v, shortcode=k, category=lo,
                                        gradeband=gradeband)
    print ek
