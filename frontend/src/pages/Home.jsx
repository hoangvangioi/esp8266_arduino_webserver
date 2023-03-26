import React, { useState, useEffect } from 'react'
import axios from "axios";
import { ReactComponent as Cloudy } from "../static/cloudy.svg";
import { ReactComponent as Day } from "../static/day.svg";
import { ReactComponent as Rainy } from "../static/rainy.svg";


const Home = () => {
    const [chart, setChart] = useState({})
    const baseUrl = process.env.REACT_APP_API_URL;

    useEffect(() => {
        const fetchCoins = async () => {
            axios.get(`${baseUrl}/dht11/last/`
            )
            .then(function (response) {
                setChart(response.data)
            })
            .catch(function (error) {
                console.log(error);
            });
        };
        fetchCoins()

    }, [baseUrl])

    let IconWeather;
    if (chart.temperature >= 25) {
        IconWeather = Day
    } else if ( chart.temperature <= 15 ) {
        IconWeather = Rainy
    } else {
        IconWeather = Cloudy
    }

    return (
        <div>
            <div className="mx-auto m-10 items-center flex flex-col md:flex-row md:justify-center w-full">
                <div className="mx-8 md:mx-0 mb-10 transition duration-500 ease-in-out transform bg-sky-200 rounded-lg hover:scale-105 cursor-pointer border flex flex-col justify-center items-center text-center p-20">
                    <div className="text-xl font-bold flex flex-col text-gray-900">
                        <span className="uppercase">In my room</span>
                        <span className="font-normal text-gray-700 text-base">Update: {chart.time}</span>
                    </div>
                    <div className="w-32 h-32 flex items-center justify-center">
                        <IconWeather width="100%" height="100%"/>
                    </div>
                    <div className="flex flex-row justify-between mt-8 space-x-5">
                        <div className="flex flex-col items-center">
                            <div className="font-medium text-base">Temperature</div>
                            <div className="text-base text-gray-500">{chart.temperature} C</div>
                        </div>
                        <div className="flex flex-col items-center">
                            <div className="font-medium text-base">Humidity</div>
                            <div className="text-base text-gray-500">{chart.humidity} %</div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    )
}

export default Home