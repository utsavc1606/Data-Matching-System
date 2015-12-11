# Data-Matching-System
System that clusters records representing the same real world entity/person into a common group based on user defined and data specific rules.
<br />
<b>Stage 1:</b> Clean the data sets to check for invalid characters and remove unwanted blank spaces.<br />
<b>Stage 2:</b> Assign record level ID's to all rows in the data set. <br />
<b>Stage 3:</b> Perform Identity Capture on the data set and build a Knowledge Base with processed clusters from the first set.<br />
<b>Stage 4:</b> Perform Identity Update on other data sets; if records already exist in Knowledge Base, fetch the cluster ID; else, put the record into a new cluster. <br />
<b>Stage 5:</b> Calculate process runtime statistics and print to log; remove personally identifiable information (eg. SSN, Name, etc)[Optional] and output de-identified data sets.
