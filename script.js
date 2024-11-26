function showTemperature(room) {
    const temperatureOutput = document.getElementById('temperature-output');
    temperatureOutput.textContent = `Loading temperature for ${room}...`;

    setTimeout(() => {
        const simulatedTemperature = `${Math.floor(Math.random() * 10) + 20}°C`; // Simulates fetching data
        temperatureOutput.textContent = `Current temperature of ${room}: ${simulatedTemperature}`;
    }, 2000);
}
