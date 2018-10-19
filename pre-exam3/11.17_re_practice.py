import re

# Guidelines
# 1. Create good and bad example strings first; mark them off manually
# 2. Use r'' strings not '' strings
# 3. Go left-to-right
# 4. Pick the right kind of "or": [ab] for single-character, (ab|cd) for longer
# 5. Optional: ()?    Several: ()*


# Python "" string, including "I use the word \"hi\" in many examples"
examples = r'''
"hi"
hi
"a string with \"hi\" in it"
"a string with "hi" in it"
a line with "just one quote
'''
strings = re.compile(r'"([^\\"]|\\.)*"')
for match in strings.finditer(examples):
    print(match.group())

ex = r'''
"match this" but not this "and this" but not this either
"tricker \"because of \"the internal quotes"
no quotes at all
'''
strings = re.compile(r'"[^"\\]*(\\.[^"\\]*)*"')
for m in strings.finditer(ex):
    print(m.group())


# addition problem: one or more numbers, separated by + or - (and maybe spaces)
ex = r'''
2
23
2+3
2 + 3
1 + 2 - 34 + 567
2 3 4
'''
addition = re.compile(r'-?[0-9]+( *[\+\-] *-?[0-9]+)*')
for match in addition.finditer(ex):
    print(match.group())


# ... and also perform the addition



# instructors on an actual Lou's List page:
# http://rabi.phys.virginia.edu/mySIS/CS2/page.php?Semester=1182&Type=Group&Group=CompSci

ex = '''useover="return overlib('Last Updated: 2017-11-17 10:04:55',AUTOSTATUS, WRAP);" onmouseout="nd();" onClick="EnrollmentGraph(1182,17266)">83 / 100</a></td><td><strong><span onmouseover="return OLgetAJAX('ldap.php?Name=Craig Dill', OLcmdIT, 300, 'ovfl1');" onmouseout="OLclearAJAX();nd();">Craig Dill</span></strong></td><td>MoWe 3:30PM - 4:45PM</td><td>Olsson Hall 120</td></tr>
<tr><td class='CourseNum'><img src='images/minus.gif' class='ICS1110 SW' onclick="toggledetails('CS1110');">&nbsp;<span onmouseover="TCFOver('1315');" onmouseout="nd();" onclick="TCF('1315');">CS 1110</span></td><td class='CourseName' colspan='7' onclick="ClassTip('CS','1110');">Introduction to Programming</td></tr>
<tr class='SectionStart T BCS1110' style='display:none'><td colspan='8'>&nbsp;</td><tr>
<tr class='SectionTitleOdd S CS1110'><td>&nbsp;</td><td colspan='8'>See http://cs1110.cs.virginia.edu/faq.html</td></tr>
<tr class='SectionOdd S CS1110'><td align='right'><a href='http://cs1110.cs.virginia.edu/faq.html'><strong>Website</strong></a>&nbsp;&nbsp;<a href='javascript:void(0);' class="Link" onclick="SectionTip('1182','17252');">17252</a>&nbsp;</td><td align='right'>001</td><td><strong>Lecture</strong> (3 Units)</td><td>Open</td><td align='right'><a href='javascript:void(0);' class="Link" onmouseover="return overlib('Last Updated: 2017-11-17 10:04:55',AUTOSTATUS, WRAP);" onmouseout="nd();" onClick="EnrollmentGraph(1182,17252)">212 / 350</a></td><td><strong><span onmouseover="return OLgetAJAX('ldap.php?Name=Luther Tychonievich', OLcmdIT, 300, 'ovfl1');" onmouseout="OLclearAJAX();nd();">Luther Tychonievich</span></strong></td><td>MoWeFr 2:00PM - 2:50PM</td><td>Chemistry Bldg 402</td></tr>
<tr class='SectionEven S CS1110'><td align='right'><a href='javascript:void(0);' class="Link" onclick="SectionTip('1182','17262');">17262</a>&nbsp;</td><td align='right'>002</td><td><strong>Lecture</strong> (3 Units)</td><td>Open</td><td align='right'><a href='javascript:void(0);' class="Link" onmouseover="return overlib('Last Updated: 2017-11-17 10:04:55',AUTOSTATUS, WRAP);" onmouseout="nd();" onClick="EnrollmentGraph(1182,17262)">97 / 148</a></td><td><strong><span onmouseover="return OLgetAJAX('ldap.php?Name=Craig Dill', OLcmdIT, 300, 'ovfl1');" onmouseout="OLclearAJAX();nd();">Craig Dill</span></strong></td><td>MoWeFr 12:00PM - 12:50PM</td><td>Olsson Hall 120</td></tr>
<tr class='SectionOdd S CS1110'><td align='right'><a href='javascript:void(0);' class="Link" onclick="SectionTip('1182','20379');">20379</a>&nbsp;</td><td align='right'>003</td><td><strong>Lecture</strong> (3 Units)</td><td>Open</td><td align='right'><a href='javascript:void(0);' class="Link" onmouseover="return overlib('Last Updated: 2017-11-17 10:04:55',AUTOSTATUS, WRAP);" onmouseout="nd();" onClick="EnrollmentGraph(1182,20379)">181 / 200</a></td><td><strong><span onmouseover="return OLgetAJAX('ldap.php?Name=Luther Tychonievich', OLcmdIT, 300, 'ovfl1');" onmouseout="OLclearAJAX();nd();">Luther Tychonievich</span></strong></td><td>MoWeFr 11:00AM - 11:50AM</td><td>Gilmer Hall 130</td></tr>
<tr class='SectionEven S CS1110'><td align='right'><a href='javascript:void(0);' class="Link" onclick="SectionTip('1182','17253');">17253</a>&nbsp;</td><td align='right'>100</td><td><strong>Laboratory</strong> (0 Units)</td><td>Wait List (8 / 199)</td><td align='right'><a href='javascript:void(0);' class="Link" onmouseover="return overlib('Last Updated: 2017-11-17 10:04:56',AUTOSTATUS, WRAP);" onmouseout="nd();" onClick="EnrollmentGraph(1182,17253)">46 / 46</a></td><td><strong><span onmouseover="return OLgetAJAX('ldap.php?Name=Luther Tychonievich', OLcmdIT, 300, 'ovfl1');" onmouseout="OLclearAJAX();nd();">Luther Tychonievich</span></strong></td><td>Th 9:30AM - 10:45AM</td><td>Olsson Hall 001</td></tr>
<tr class='SectionOdd S CS1110'><td align='right'><a href='javascript:void(0);' class="Link" onclick="SectionTip('1182','17254');">17254</a>&nbsp;</td><td align='right'>101</td><td><strong>Laboratory</strong> (0 Units)</td><td>Wait List (11 / 199)</td><td align='right'><a href='javascript:void(0);' class="Link" onmouseover="return overlib('Last Updated: 2017-11-17 10:04:56',AUTOSTATUS, WRAP);" onmouseout="nd();" onClick="EnrollmentGraph(1182,17254)">46 / 46</a></td><td><strong><span onmouseover="return OLgetAJAX('ldap.php?Name=Luther Tychonievich', OLcmdIT, 300, 'ovfl1');" onmouseout="OLclearAJAX();nd();">Luther Tychonievich</span></strong></td><td>Th 11:00AM - 12:15PM</td><td>Olsson Hall 001</td></tr>
<tr class='SectionEven S CS1110'><td align='right'><a href='javascript:void(0);' class="Link" onclick="SectionTip('1182','17255');">17255</a>&nbsp;</td><td align='right'>102</td><td><strong>Laboratory</strong> (0 Units)</td><td>Wait List (6 / 199)</td><td align='right'><a href='javascript:void(0);' class="Link" onmouseover="return overlib('Last Updated: 2017-11-17 10:04:56',AUTOSTATUS, WRAP);" onmouseout="nd();" onClick="EnrollmentGraph(1182,17255)">46 / 46</a></td><td><strong><span onmouseover="return OLgetAJAX('ldap.php?Name=Luther Tychonievich', OLcmdIT, 300, 'ovfl1');" onmouseout="OLclearAJAX();nd();">Luther Tychonievich</span></strong></td><td>Th 12:30PM - 1:45PM</td><td>Olsson Hall 001</td></tr>
<tr class='SectionOdd S CS1110'><td align='right'><a href='javascript:void(0);' class="Link" onclick="SectionTip('1182','17256');">17256</a>&nbsp;</td><td align='right'>103</td><td><strong>Laboratory</strong> (0 Units)</td><td>Wait List (6 / 199)</td><td align='right'><a href='javascript:void(0);' class="Link" onmouseover="return overlib('Last Updated: 2017-11-17 10:04:56',AUTOSTATUS, WRAP);" onmouseout="nd();" onClick="EnrollmentGraph(1182,17256)">46 / 46</a></td><td><strong><span onmouseover="return OLgetAJAX('ldap.php?Name=Luther Tychonievich', OLcmdIT, 300, 'ovfl1');" onmouseout="OLclearAJAX();nd();">Luther Tychonievich</span></strong></td><td>Th 2:00PM - 3:15PM</td><td>Olsson Hall 001</td></tr>
<tr class='SectionEven S CS1110'><td align='right'><a href='javascript:void(0);' class="Link" onclick="SectionTip('1182','17257');">17257</a>&nbsp;</td><td align='right'>104</td><td><strong>Laboratory</strong> (0 Units)</td><td>Wait List (5 / 199)</td><td align='right'><a href='javascript:void(0);' class="Link" onmouseover="return overlib('Last Updated: 2017-11-17 10:04:56',AUTOSTATUS, WRAP);" onmouseout="nd();" onClick="EnrollmentGraph(1182,17257)">46 / 46</a></td><td><strong><span onmouseover="return OLgetAJAX('ldap.php?Name=Luther Tychonievich', OLcmdIT, 300, 'ovfl1');" onmouseout="OLclearAJAX();nd();">Luther Tychonievich</span></strong></td><td>Th 3:30PM - 4:45PM</td><td>Olsson Hall 001</td></tr>
<tr class='SectionOdd S CS1110'><td align='right'><a href='javascript:void(0);' class="Link" onclick="SectionTip('1182','17258');">17258</a>&nbsp;</td><td align='right'>105</td><td><strong>Laboratory</strong> (0 Units)</td><td>Wait List (0 / 199)</td><td align='right'><a href='javascript:void(0);' class="Link" onmouseover="return overlib('Last Updated: 2017-11-17 10:04:56',AUTOSTATUS, WRAP);" onmouseout="nd();" onClick="EnrollmentGraph(1182,17258)">46 / 46</a></td><td><strong><span onmouseover="return OLgetAJAX('ldap.php?Name=Luther Tychonievich', OLcmdIT, 300, 'ovfl1');" onmouseout="OLclearAJAX();nd();">Luther Tychonievich</span></strong></td><td>Th 5:00PM - 6:15PM</td><td>Olsson Hall 001</td></tr>
<tr class='SectionEven S CS1110'><td align='right'><a href='javascript:void(0);' class="Link" onclick="SectionTip('1182','17259');">17259</a>&nbsp;</td><td align='right'>106</td><td><strong>Laboratory</strong> (0 Units)</td><td>Open</td><td align='right'><a href='javascript:void(0);' class="Link" onmouseover="return overlib('Last Updated: 2017-11-17 10:04:56',AUTOSTATUS, WRAP);" onmouseout="nd();" onClick="EnrollmentGraph(1182,17259)">30 / 46</a></td><td><strong><span onmouseover="return OLgetAJAX('ldap.php?Name=Luther Tychonievich', OLcmdIT, 300, 'ovfl1');" onmouseout="OLclearAJAX();nd();">Luther Tychonievich</span></strong></td><td>Th 6:30PM - 7:45PM</td><td>Olsson Hall 001</td></tr>
<tr class='SectionOdd S CS1110'><td align='right'><a href='javascript:void(0);' class="Link" onclick="SectionTip('1182','17260');">17260</a>&nbsp;</td><td align='right'>107</td><td><strong>Laboratory</strong> (0 Units)</td><td>Wait List (1 / 199)</td><td align='right'><a href='javascript:void(0);' class="Link" onmouseover="return overlib('Last Updated: 2017-11-17 10:04:56',AUTOSTATUS, WRAP);" onmouseout="nd();" onClick="EnrollmentGraph(1182,17260)">48 / 48</a></td><td><strong><span onmouseover="return OLgetAJAX('ldap.php?Name=Luther Tychonievich', OLcmdIT, 300, 'ovfl1');" onmouseout="OLclearAJAX();nd();">Luther Tychonievich</span></strong></td><td>Th 11:00AM - 12:15PM</td><td>Mechanical Engr Bldg 213</td></tr>
<tr class='SectionEven S CS1110'><td align='right'><a href='javascript:void(0);' class="Link" onclick="SectionTip('1182','17261');">17261</a>&nbsp;</td><td align='right'>108</td><td><strong>Laboratory</strong> (0 Units)</td><td>Wait List (6 / 199)</td><td align='right'><a href='javascript:void(0);' class="Link" onmouseover="return overlib('Last Updated: 2017-11-17 10:04:56',AUTOSTATUS, WRAP);" onmouseout="nd();" onClick="EnrollmentGraph(1182,17261)">48 / 48</a></td><td><strong><span onmouseover="return OLgetAJAX('ldap.php?Name=Luther Tychonievich', OLcmdIT, 300, 'ovfl1');" onmouseout="OLclearAJAX();nd();">Luther Tychonievich</span></strong></td><td>Th 3:30PM - 4:45PM</td><td>Mechanical Engr Bldg 213</td></tr>
<tr class='SectionOdd S CS1110'><td align='right'><a href='javascript:void(0);' class="Link" onclick="SectionTip('1182','17263');">17263</a>&nbsp;</td><td align='right'>109</td><td><strong>Laboratory</strong> (0 Units)</td><td>Wait List (0 / 199)</td><td align='right'><a href='javascript:void(0);' class="Link" onmouseover="return overlib('Last Updated: 2017-11-17 10:04:56',AUTOSTATUS, WRAP);" onmouseout="nd();" onClick="EnrollmentGraph(1182,17263)">48 / 48</a></td><td><strong><span onmouseover="return OLgetAJAX('ldap.php?Name=Luther Tychonievich', OLcmdIT, 300, 'ovfl1');" onmouseout="OLclearAJAX();nd();">Luther Tychonievich</span></strong></td><td>Th 5:00PM - 6:15PM</td><td>Mechanical Engr Bldg 213</td></tr>
<tr class='SectionEven S CS1110'><td align='right'><a href='javascript:void(0);' class="Link" onclick="SectionTip('1182','17391');">17391</a>&nbsp;</td><td align='right'>110</td><td><strong>Laboratory</strong> (0 Units)</td><td>Open</td><td align='right'><a href='javascript:void(0);' class="Link" onmouseover="return overlib('Last Updated: 2017-11-17 10:04:56',AUTOSTATUS, WRAP);" onmouseout="nd();" onClick="EnrollmentGraph(1182,17391)">19 / 48</a></td><td><strong><span onmouseover="return OLgetAJAX('ldap.php?Name=Luther Tychonievich', OLcmdIT, 300, 'ovfl1');" onmouseout="OLclearAJAX();nd();">Luther Tychonievich</span></strong></td><td>Th 6:30PM - 7:45PM</td><td>Mechanical Engr Bldg 213</td></tr>
<tr class='SectionOdd S CS1110'><td align='right'><a href='javascript:void(0);' class="Link" onclick="SectionTip('1182','20380');">20380</a>&nbsp;</td><td align='right'>111</td><td><strong>Laboratory</strong> (0 Units)</td><td>Open</td><td align='right'><a href='javascript:void(0);' class="Link" onmouseover="return overlib('Last Updated: 2017-11-17 10:04:56',AUTOSTATUS, WRAP);" onmouseout="nd();" onClick="EnrollmentGraph(1182,20380)">21 / 100</a></td><td><strong><span onmouseover="return OLgetAJAX('ldap.php?Name=Luther Tychonievich', OLcmdIT, 300, 'ovfl1');" onmouseout="OLclearAJAX();nd();">Luther Tychonievich</span></strong></td><td>Th 5:00PM - 6:15PM</td><td>Rice Hall 130</td></tr>
<tr><td class='CourseNum'><img src='images/minus.gif' class='ICS1111 SW' onclick="toggledetails('CS1111');">&nbsp;<span onmouseover="TCFOver('1316');" onmouseout="nd();" onclick="TCF('1316');">CS 1111</span></td><td class='CourseName' colspan='7' onclick="ClassTip('CS','1111');">Introduction to Programming</td></tr>
<tr class='SectionStart T BCS1111' style='display:none'><td colspan='8'>&nbsp;</td><tr>
<tr class='SectionOdd S CS1111'><td align='right'><a href='javascript:void(0);' class="Link" onclick="SectionTip('1182','17264');">17264</a>&nbsp;</td><td align='right'>001</td><td><strong>Lecture</strong> (3 Units)</td><td>Wait List (1 / 199)</td><td align='right'><a href='javascript:void(0);' class="Link" onmouseover="return overlib('Last Updated: 2017-11-17 10:04:56',AUTOSTATUS, WRAP);" onmouseout="nd();" onClick="EnrollmentGraph(1182,17264)">75 / 75</a></td><td><strong><span onmouseover="return OLgetAJAX('ldap.php?Name=Upsorn Praphamontripong', OLcmdIT, 300, 'ovfl1');" onmouseout="OLclearAJAX();nd();">Upsorn Praphamontripong</span></strong></td><td>MoWe 2:00PM - 3:15PM</td><td>Olsson Hall 005</td></tr>
<tr><td class='CourseNum'><img src='images/minus.gif' class='ICS1112 SW' onclick="toggledetails('CS1112');">&nbsp;<span onmouseover="TCFOver('1317');" onmouseout="nd();" onclick="TCF('1317');">CS 1112</span></td><td class='CourseName' colspan='7' onclick="ClassTip('CS','1112');">Introduction to Programming</td></tr>
<tr class='SectionStart T BCS1112' style='display:none'><td colspan='8'>&nbsp;</td><tr>
<tr class='SectionTitleOdd S CS1112'><td>&nbsp;</td><td colspan='8'>To see what CS 111X course is right you, check out www.tinyurl.com/choosing-a-cs-111x </td></tr>
<tr class='SectionOdd S CS1112'><td align='right'><a href='http://www.cs1112.org/term/181'><strong>Website</strong></a>&nbsp;&nbsp;<a href='javascript:void(0);' class="Link" onclick="SectionTip('1182','17265');">17265</a>&nbsp;</td><td align='right'>001</td><td><strong>Lecture</strong> (3 Units)</td><td>Open</td><td align='right'><a href='javascript:void(0);' class="Link" onmouseover="return overlib('Last Updated: 2017-11-17 10:04:56',AUTOSTATUS, WRAP);" onmouseout="nd();" onClick="EnrollmentGraph(1182,17265)">120 / 145</a></td><td><strong><span onmouseover="return OLgetAJAX('ldap.php?Name=James Cohoon', OLcmdIT, 300, 'ovfl1');" onmouseout="OLclearAJAX();nd();">James Cohoon</span></strong></td><td>MoWeFr 2:00PM - 3:15PM</td><td>Rice Hall 130</td></tr>
<tr><td class='CourseNum'><img src='images/minus.gif' class='ICS1113 SW' onclick="toggledetails('CS1113');">&nbsp;<span onmouseover="TCFOver('8427');" onmouseout="nd();" onclick="TCF('8427');">CS 1113</span></td><td class='CourseName' colspan='7' onclick="ClassTip('CS','1113');">Introduction to Programming</td></tr>
<tr class='SectionStart T BCS1113' style='display:none'><td colspan='8'>&nbsp;</td><tr>
<tr class='SectionOdd S CS1113'><td align='right'><a href='javascript:void(0);' class="Link" onclick="SectionTip('1182','18246');">18246</a>&nbsp;</td><td align='right'>001</td><td><strong>Lecture</strong> (3 Units)</td><td>Open<span onmouseover="return overlib('Enrollment Requirements: Undergraduate Arts & Sciences',AUTOSTATUS, WRAP);" onmouseout="nd();"> <img src='images/r.png'></span></td><td align='right'><a href='javascript:void(0);' class="Link" onmouseover="return overlib('Last Updated: 2017-11-17 10:04:56',AUTOSTATUS, WRAP);" onmouseout="nd();" onClick="EnrollmentGraph(1182,18246)">9 / 80</a></td><td><strong><span onmouseover="return OLgetAJAX('ldap.php?Name=Kevin Sullivan', OLcmdIT, 300, 'ovfl1');" onmouseout="OLclearAJAX();nd();">Kevin Sullivan</span></strong></td><td>MoWeFr 11:00AM - 11:50AM</td><td>Thornton Hall E316</td></tr>
<tr class='SectionOdd S CS1113'><td></td><td></td><td></td><td></td><td></td><td><strong>Kevin Sullivan</strong></td><td>Th 5:00PM - 6:15PM</td><td>Olsson Hall 005</td></tr>
<tr class='SectionTitleEven S CS1113'><td>&nbsp;</td><td colspan='8'>CS1113-002 </td></tr>
<tr class='SectionEven S CS1113'><td align='right'><a href='https://goo.gl/rJj51d'><strong>Website</strong></a>&nbsp;&nbsp;<a href='javascript:void(0);' class="Link" onclick="SectionTip('1182','21888');">21888</a>&nbsp;</td><td align='right'>002</td><td><strong>Lecture</strong> (3 Units)</td><td>Open<span onmouseover="return overlib('Enrollment Requirements: 1st-Year Engineering',AUTOSTATUS, WRAP);" onmouseout="nd();"> <img src='images/r.png'></span></td><td align='right'><a href='javascript:void(0);' class="Link" onmouseover="return overlib('Last Updated: 2017-11-17 10:04:56',AUTOSTATUS, WRAP);" onmouseout="nd();" onClick="EnrollmentGraph(1182,21888)">0 / 50</a></td><td><strong><span onmouseover="return OLgetAJAX('ldap.php?Name=Qureshi Asma', OLcmdIT, 300, 'ovfl1');" onmouseout="OLclearAJAX();nd();">Qureshi Asma</span></strong></td><td>MoWeFr 1:00PM - 1:50PM</td><td>Olsson Hall 011</td></tr>
<tr class='SectionEven S CS1113'><td></td><td></td><td></td><td></td><td></td><td><strong>Qureshi Asma</strong></td><td>Tu 5:00PM - 6:15PM</td><td>Olsson Hall 005</td></tr>
<tr class='SectionTitleEven S CS1113'><td>&nbsp;</td><td colspan='8' class='TextWidth'>Please visit this link (https://goo.gl/rJj51d) for tentative syllabus and topics and feel free to contact me (fa5ar@virginia.edu) if you have any questions.
'''

instructors = re.compile(r"'ldap.php\?Name=([^']+)'")
for match in instructors.finditer(ex):
    print(match.group(1))