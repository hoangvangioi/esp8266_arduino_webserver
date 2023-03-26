import React from 'react'
import AreaChart from '../Charts/AreaChart';


const Light = () => {

    return (
        <>
            <AreaChart apiUrl="light/" value_1="intensity" value_2="time" />
        </>
    )
}

export default Light