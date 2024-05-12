function updateDateTime() {
    const currentDate = new Date();
  
    const monthNames = [
      'Janvier', 'Février', 'Mars', 'Avril', 'Mai', 'Juin',
      'Juillet', 'Août', 'Septembre', 'Octobre', 'Novembre', 'Décembre'
      ];
  
    const year = currentDate.getFullYear();
    const month = monthNames[currentDate.getMonth()];
    const day = currentDate.getDate().toString().padStart(2, '0');
  
    const hours = currentDate.getHours().toString().padStart(2, '0');
    const minutes = currentDate.getMinutes().toString().padStart(2, '0');
    const seconds = currentDate.getSeconds().toString().padStart(2, '0');
  
    const formattedDate = ` ${day} ${month} ${year}`;
    const formattedTime = `${hours}:${minutes}:${seconds}`;
  
    const currentDateTimeElement = document.getElementById('currentDateTime');
    currentDateTimeElement.textContent = `${formattedDate} ${formattedTime}`;
  }
  
  // Update date and time immediately
  updateDateTime();
  
  // Update date and time every second
  setInterval(updateDateTime, 1000);
  