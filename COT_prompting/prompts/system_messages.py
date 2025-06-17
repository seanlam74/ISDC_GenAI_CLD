# system_messages.py

# Step 1: Instructional overview (Prompt 1)

prompt_1 = ([
    # Prompt 1 for understanding the task at hand
    """
    Your task is to aid a team of system dynamics modellers by a generating Causal Loop Diagrams  Specification (CLDS), which consists of a Node List and an Edge List, from a textual description of a system. The textual description is called the Dynamic Hypotheses Input (DHI).  The task of generating a CLDS from a DHI has two parts: 
    (i)	generation of system variables, specified as a Node List, from the DHI. 
    Note that the variables are generally nouns, with a sense of direction. A sense of direction means that, for example, “Morale” is better than “Mental Attitude”, because with morale we know that higher generally is better.
    (ii)	generation of a directed graph (which completes the CLDS), specified by the Node List and an Edge List, from the DHI. 
    Note that the Edge List shows relationships between the variables in the Node List. Only two types of relationships exist: positive (shown by 1) and negative links (shown by -1). 
    
    A positive link from variable X to variable Y means that other things being constant, increasing X would change Y to a level above what it would otherwise have been and decreasing X would change Y to a level below what it would otherwise have been. 
    
    A negative link from variable X to variable Y means that other things being constant, increasing X would change Y to a level below what it would otherwise have been and decreasing X would change Y to a level above what it would otherwise have been. 

    The steps to follow are the following:
    
    For Case 1 and Case 2,
        1.	The modelling team will give you the DHI and ask you to confirm that you have understood it.
        2.	Then the modelling team will give you the Node List. 
        3.	Finally, the modelling team will provide you with the Edge List.
    
    Use Cases 1 and 2 to internalize the generation of the CLDS from the DHI.

    For Case 3 and other cases in the future:
        1.	The modelling team will give you the DHI.
        2.	You are to generate a proposed Node List. 
        3.	The modelling team will review this list and provide you a corrected Node List. 
        4.	You are to generate the Edge List.
        5.	The modelling team will provide you with the corrected Edge List.

    Case 1, Case 2, and Case 3 have increasing complexity. 
    
    Is this overall flow clear? 
    """])

# Step 2: Simple use case (Case 1) [Prompt 2 + 3]

prompt_2 = ([
    # Prompt 2 establishes the basic mechanism of CLDS construction with a simple use case.
    # By completing Case 1, the LLM should gain some familiarity with the syntax and logic of causal diagrams.
    """
    Prompt 2 establishes the basic mechanism of CLDS construction with a simple use case. By completing Case 1, the LLM should gain some familiarity with the syntax and logic of causal diagrams. Prompt 2 is as follows:
    
    Let’s follow the flow and start with Case 1. 
    
    Case 1 DHI: Births and deaths

    An increase in fertility (births per population) means the birth rate (in people per year) will increase above what it would otherwise have been, and a decrease in fertility means the birth rate will fall below what it would otherwise have been. In short: fertility is positively linked to birth rate. 

    Average lifetime (years lived per person) is negatively linked to death rate (people per year). Birth rate to population is a positive link; Population to birth rate is a positive link. Population to death rate is a direct relationship; Death rate to population is an inverse relationship.
    """
])

prompt_3 = ([
    # Prompt 3 provides the LLM with the Node and Edge Lists for Case 1
    """
    Prompt 3 provides the LLM with the Node and Edge Lists for Case 1 as follows:

    Case 1 Node List
    Node.ID,	Node.Description
    01,	Fertility
    02,	Birth rate
    03,	Population
    04,	Death rate
    05,	Average lifetime

    Case 1 Edges List
    Source.Node.ID,	Sink.Node.ID,	Value
    01,	02,	1
    02,	03,	1
    03,	02,	1
    03,	04,	1
    04,	03,	-1
    05,	04,	-1

    Is Case 1 clear? 

    """
])

# Step 3: Moderate complexity (Case 2) [Prompt 4 + 5]
prompt_4 =([
    # Prompt 4 introduces the Susceptible-Infectious-Recovered (SIR) Model to the LLm and expands the complexity with population compartments and additional factors
    """
    Now let’s move to Case 2. Case 2 DHI: Susceptible Infectious Recovered (SIR) Model:

    The total population of an island determines the initial “susceptible population” (i.e., those can be infected). Those contracting the infection become infectious (join “infectious population”) for a period of time, but then recover (join “recovered population”) and develop permanent immunity. Contact rate is the rate of interaction in the community, or people contacted per person per time. Infectivity is the probability that the disease is transmitted when a susceptible person contacts an infection person. The infection rate, i.e., people infected per day, is directly proportional to susceptible population, (infectious population/total population), infectivity, and contact rate. The infectious population increases as the infection rate increases; the susceptible population decreases as infection rate increases. Recovery rate (that is, people recovering per unit time), increases with infectious population, but decreases with average duration of infectivity. Recovery rate reduces the infectious population, and increases the recovered population.
    """
])

prompt_5 = ([
    # Prompt 5 provides the nodes and edge lists to the LLM for Case 2
    """
    Case 2 Node List
    
    Node.ID,	Node.Description
    01,	Susceptible population
    02,	Infectious population
    03,	Recovered population
    04,	Total population
    05,	Infectivity
    06,	Contact rate
    07,	Infection rate
    08,	Avg duration of infectivity
    09,	Recovery rate

    Case 2 Edges List

    Source.Node.ID,	Sink.Node.ID,	Value
    01,	07,	1
    02,	07,	1
    02,	09,	1
    04,	01,	1
    04,	07,	-1
    05,	07,	1
    06,	07,	1
    07,	01,	-1
    07,	02,	1
    08,	09,	-1
    09,	02,	-1
    09,	03,	1
    """
])

prompt_6 = ([
    # Prompt 6 provides the Dynamic Hypotheses Input (DHI) for test case
    """
    Now you need to work on Case 3.
    
    Case 3 DHI: Acute Hospital Use
    Rising population level, together with population ageing, cause an increase in the chronic disease burden as well as the burden of frailty in Singapore. These two burdens both translate into three types of needs: (i) acute care needs (ii) sub-acute care needs (iii) rehab needs. Acute care needs drive unavoidable Length of Stay (LOS) in Acute Hospitals (AHs), while sub-acute needs drive Avoidable LOS. (Note: LOS is considered avoidable when the stay could have been “decanted” to a site other than an AH). Rehab needs drive both unavoidable and avoidable LOS. Avoidable LOS drives avoidable AH inpatient-days, and unavoidable LOS drives unavoidable AH inpatient-days. Avoidable and unavoidable inpatient-days together affect AH beds required. 
    AH capacity gap is directly driven by AH beds required; on the other hand AH beds required is positively linked to AH capacity increases, which is negatively linked to AH capacity gap. AH capacity gap drives waiting time for AH beds, which drives unmet needs, which increases chronic disease burden and the burden of frailty. 
    Burden of frailty and chronic disease burden drive AH inpatient admissions, which is positively linked to both Avoidable and unavoidable AH inpatient-days.
    
    Provide me your Node List
    """
])

prompt_7 = ([
    # Prompt 7 provides the guidelines for the corrected node list prior to the generation of the edges in the CLD
    """
    This is the corrected Case 3 Node List.

    Node.ID,	Node.Description
    A01,	Population
    A02,	Population ageing
    A03,	Chronic Disease Burden
    A04,	Burden of frailty
    A05a,	Acute care needs
    A05b,	Rehab care needs
    A05c,	Sub-acute care needs
    A06a,	Unavoidable AH LOS
    A06b,	Avoidable AH LOS
    A07a,	Unavoidable AH inpatient-days
    A07b,	Avoidable AH inpatient-days
    A08,	AH beds required
    A09,	AH capacity increases
    A10,	AH capacity gap
    A11,	Waiting time for AH beds
    A12,	Unmet needs
    A13,	AH inpatient admissions
    """
])

prompt_8 = ([
    # Prompt 8 request for the development of the final edge list in an output
    """
    Using the corrected Node List, provide me the Edges List, formatted so that it is easy to copy into a spreadsheet.
    """
])

# Flattened prompt sequence for chaining
PROMPT_SEQUENCE = [
    prompt_1[0],
    prompt_2[0],
    prompt_3[0],
    prompt_4[0],
    prompt_5[0],
    prompt_6[0],
    prompt_7[0],
    prompt_8[0],
]