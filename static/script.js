async function predictAQI() {
    const city = document.getElementById('cityInput').value;
    if (!city) {
        document.getElementById('result').innerHTML = 'Please enter a city name';
        return;
    }

    try {
        const response = await fetch('/predict', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ city })
        });

        const data = await response.json();
        if (response.ok) {
            let resultHtml = `<h2>Air Quality Report for ${data.city}</h2>`;
            resultHtml += '<div class="result-details">';
            resultHtml += `<p><strong>AQI:</strong> ${data.aqi || 'N/A'}</p>`;
            resultHtml += `<p><strong>PM2.5:</strong> ${data.pm25 !== null ? data.pm25 : 'N/A'} µg/m³</p>`;
            resultHtml += `<p><strong>PM10:</strong> ${data.pm10 !== null ? data.pm10 : 'N/A'} µg/m³</p>`;
            resultHtml += `<p><strong>NO2:</strong> ${data.no2 !== null ? data.no2 : 'N/A'} µg/m³</p>`;
            resultHtml += `<p><strong>SO2:</strong> ${data.so2 !== null ? data.so2 : 'N/A'} µg/m³</p>`;
            resultHtml += `<p><strong>CO:</strong> ${data.co !== null ? data.co : 'N/A'} mg/m³</p>`;
            resultHtml += `<p><strong>O3:</strong> ${data.o3 !== null ? data.o3 : 'N/A'} µg/m³</p>`;
            resultHtml += `<p><strong>AQI Category:</strong> ${data.condition}</p>`;
            resultHtml += '</div>';

            document.getElementById('result').innerHTML = resultHtml;
        } else {
            document.getElementById('result').innerHTML = `Error: ${data.error}`;
        }
    } catch (error) {
        document.getElementById('result').innerHTML = 'Error: Could not connect to server';
    }
}