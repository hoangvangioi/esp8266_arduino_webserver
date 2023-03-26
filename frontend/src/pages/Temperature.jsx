import React from 'react'
import AreaChart from '../Charts/AreaChart';


const Temperature = () => {
    return (
        <>
            <AreaChart apiUrl="dht11/" value_1="temperature" value_2="time" />
        </>
    )
}

export default Temperature