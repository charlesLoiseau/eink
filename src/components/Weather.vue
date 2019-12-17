<template>
  <div>
    <h1>MIN {{ daily.Temperature.Maximum.Value }} °C</h1>
    <h1>MAX {{ daily.Temperature.Minimum.Value }} °C</h1>
    <h3></h3>
  </div>
</template>

<script>
import axios from 'axios';

async function getDailyWeather() {
    const response = await axios.get("http://dataservice.accuweather.com/forecasts/v1/daily/1day/133651?apikey=NZkRfJXuglJmtR6vYgdZFZ5bB6PfJAbV&metric=true")
    // eslint-disable-next-line no-unused-vars
    return response.data.DailyForecasts[0]

}
async function getHourlyWeather() {
    const response = await axios.get("http://dataservice.accuweather.com/forecasts/v1/hourly/12hour/133651?apikey=NZkRfJXuglJmtR6vYgdZFZ5bB6PfJAbV&metric=true")
    return response.data
}
export default {
    data() {
        return {
            hourly: undefined,
            daily: undefined
        }
    },
    computed: {
    
    },
    mounted() {
        getHourlyWeather().then((data) => {
            this.hourly = data
        })
        getDailyWeather().then((data) => {
            this.daily = data

        })

    },


}
</script>

<style>

</style>