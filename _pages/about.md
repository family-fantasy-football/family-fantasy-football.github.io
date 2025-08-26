---
layout: about
title: home
permalink: /
# subtitle: <a href='#'>Affiliations</a>. Address. Contacts. Motto. Etc.

profile:
  align: center
  image:
  image_circular: false # crops the image to make it circular
  more_info:

news: true # includes a list of news items
selected_papers: false
social: false # includes social icons at the bottom of the page
pretty_table: True
chart:
  echarts: true
---

## Welcome to the site for the Family Fantasy Footbal League! We are currently in the offseason.

<div style="margin-bottom: 30px;">

</div>

<div id="countdown-container" style="text-align: center; margin: 30px 0; padding: 20px; background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); border-radius: 10px; color: white;">
    <h3 style="margin-bottom: 15px;">Countdown to Draft</h3>
    <div id="countdown" style="font-size: 2em; font-weight: bold;">
        <span id="days">00</span>d 
        <span id="hours">00</span>h 
        <span id="minutes">00</span>m 
        <span id="seconds">00</span>s
    </div>
</div>

<script>
function updateCountdown() {
    const targetDate = new Date("2025-09-02T19:00:00").getTime();
    const now = new Date().getTime();
    const difference = targetDate - now;
    
    if (difference > 0) {
        const days = Math.floor(difference / (1000 * 60 * 60 * 24));
        const hours = Math.floor((difference % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
        const minutes = Math.floor((difference % (1000 * 60 * 60)) / (1000 * 60));
        const seconds = Math.floor((difference % (1000 * 60)) / 1000);
        
        document.getElementById('days').textContent = days.toString().padStart(2, '0');
        document.getElementById('hours').textContent = hours.toString().padStart(2, '0');
        document.getElementById('minutes').textContent = minutes.toString().padStart(2, '0');
        document.getElementById('seconds').textContent = seconds.toString().padStart(2, '0');
    } else {
        document.getElementById('countdown').innerHTML = '<span style="font-size: 1.2em;">Season Started!</span>';
    }
}

updateCountdown();
setInterval(updateCountdown, 1000);
</script>

Last year's top scorer is: Kyle Hamlin (1762.02)

Last year's bottom scorer is: Abbey Hamlin and Christine Hamlin (1438.72)

Last year's Highest Scoring Week: Kyle Hamlin - 180.62 points (Week 6)

Last year's Lowest Scoring Week: Abbey Hamlin and Christine Hamlin - 73.28 points (Week 7)

Last year's Luckiest Team: Abbey Hamlin and Christine Hamlin (0.9) Wins Above Expected

Last year's Unluckiest Team: Ryan Ratcliff (-3.1) Wins Below Expected


