import React from 'react'
import AreaChart from '../Charts/AreaChart';


const Humidity = () => {

    return (
        <>
            <AreaChart apiUrl="dht11/" value_1="humidity" value_2="time" />
        </>
    )
}

export default Humidity