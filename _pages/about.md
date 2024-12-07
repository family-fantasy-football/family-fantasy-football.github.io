---
layout: about
title: home
permalink: /
# subtitle: <a href='#'>Affiliations</a>. Address. Contacts. Motto. Etc.

profile:
  align: right
  image: prof_pic.jpg
  image_circular: false # crops the image to make it circular
  more_info: >
    <p>555 your office number</p>
    <p>123 your address street</p>
    <p>Your City, State 12345</p>

news: false # includes a list of news items
selected_papers: false # includes a list of papers marked as "selected={true}"
social: false # includes social icons at the bottom of the page
---

<!--
<table id="standings" data-toggle="table" data-url="{{ '/assets/standings.json' | relative_url }}">
  <thead>
    <tr>
      <th data-field="team">Team</th>
      <th data-field="record">Record</th>
      <th data-field="last3">Last 3 Games</th>
    </tr>
  </thead>
</table> -->

<table 
 data-click-to-select="true"
 data-height="460"
 data-pagination="true" 
 data-search="true"
 data-toggle="table"
 data-url="{{ "/assets/json/standings.json"}}">
 <thead>
   <tr>
     <th data-checkbox="true"></th>
     <th data-field="team" data-halign="left" data-align="center" data-sortable="true">Team</th>
     <th data-field="record" data-halign="center" data-align="right" data-sortable="true">Record</th>
     <th data-field="last3" data-halign="right" data-align="left" data-sortable="true">Last 3 Games</th>
   </tr>
 </thead>
</table>
