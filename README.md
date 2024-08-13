# Studio5000-Settings-Initializer
Parameters:
This CMDL program will prompt you for:
- a c** type. It could be phase, digital input, digital output, and .... This will be a numeric entry.
- an excel file which has the format detailed below
- Two keywords which you must specify (before after) (more detail below)

This is an example table below.
Some crucial details to formatting your excel file are  Have an equal number of "Before Names" and "After Names". They need to be in order respectively in the Name column The before names must have a matching keyword that is able to differentiate between the before and after.
For example:

If on the top you have:
BeforeValve1
BeforeValve2
BeforeValve6
BeforeValve9
Then on the bottom, you must have:
AfterValve1
AfterValve2
AfterValve6
AfterValve9

In the table this would look like:

Name
BeforeValve1
BeforeValve2
BeforeValve6
BeforeValve9
AfterValve1
AfterValve2
AfterValve6
AfterValve9

Your before keyword here would be "Before" and your after keyword would be "After"
Fill in the base tags with the appropriate tags. Add a type column, and then after that continue adding as many extensions as required. For example TMR[0].PRE or COUNTER.PRE
+----------------+-------------+--------+---------------------------------+
|      Name      |  Base Tags  |  Type  |   Extension1   |   Extension2   |
+----------------+-------------+--------+----------------+----------------+
|   Mixer 31     | cY[X1]      | Z1     |     Value1A    |     Value2A    |
+----------------+-------------+--------+----------------+----------------+
|   Mixer 31     | cY[X2]      | Z2     |     Value1B    |     Value2B    |
+----------------+-------------+--------+----------------+----------------+
|   Mixer 11     | cY[X3]      |  Z3    |     Value1C    |     Value2C    |
+----------------+-------------+--------+----------------+----------------+
|   Mixer 11     | cY[X4]      |    Z4  |     Value1D    |     Value2D    |
+----------------+-------------+--------+----------------+----------------+
