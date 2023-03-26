import React from 'react'
import AreaChart from '../Charts/AreaChart'


const WaterLevel = () => {
    return (
        <>
            <AreaChart apiUrl="water/" value_1="water_level" value_2="time" />
        </>
    )
}

export default WaterLevel