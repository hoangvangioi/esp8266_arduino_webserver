import React from 'react'
import AreaChart from '../Charts/AreaChart';


const Sound = () => {
    return (
        <>
            <AreaChart apiUrl="sound/" value_1="intensity" value_2="time" />
        </>
    )
}

export default Sound