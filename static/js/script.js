document.addEventListener("DOMContentLoaded", function() {
    // ดึงข้อมูลจาก API
    fetch("http://localhost:5000/api/temperature")
        .then(response => response.json())
        .then(data => {
            // นำข้อมูลมาแสดงบนตาราง
            const temperatureData = document.getElementById("temperature-data");
            data.forEach(entry => {
                const row = temperatureData.insertRow();
                row.insertCell(0).textContent = entry.id;
                row.insertCell(1).textContent = entry.sensor_name;
                row.insertCell(2).textContent = entry.date_time;
                row.insertCell(3).textContent = entry.Temperature;
            });
        })
        .catch(error => {
            console.error("เกิดข้อผิดพลาดในการดึงข้อมูล: " + error);
        });
});


document.addEventListener("DOMContentLoaded", function() {
    // ดึงข้อมูลจาก API
    fetch("http://localhost:5000/api/humidity")
        .then(response => response.json())
        .then(data => {
            // นำข้อมูลมาแสดงบนตาราง
            const humidityData = document.getElementById("humidity-data");
            data.forEach(entry => {
                const row = humidityData.insertRow();
                row.insertCell(0).textContent = entry.id;
                row.insertCell(1).textContent = entry.sensor_name;
                row.insertCell(2).textContent = entry.date_time;
                row.insertCell(3).textContent = entry.Humidity;
            });
        })
        .catch(error => {
            console.error("เกิดข้อผิดพลาดในการดึงข้อมูล: " + error);
        });
});
