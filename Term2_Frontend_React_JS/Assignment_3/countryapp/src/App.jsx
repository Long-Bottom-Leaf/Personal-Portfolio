import React, {useEffect, useState} from 'react';
import NeighboursA from './components/NeighboursA';
import NeighboursI from './components/NeighboursI';

import './App.css'

function App() {
  const [displayA, setCountryA] = useState(false);            // initially set displayA/I as false
  const [displayI, setCountryI] = useState(false);

  const [countries, setCountries] = useState([]);             // initiate countries as an empty array
  const [codeToNameMap, setCodeToNameMap] = useState({});     // initiate countrie code to map as an empty value

  // fetch countries from the API
    useEffect(() => {
      const fetchCountries = async () => {
        try {
          const res = await fetch(`https://restcountries.com/v3.1/all?fields=name,capital,flags,borders,cca3`); // I had to use a more specific URL query cause the one provided was returning a 400 error
          const data = await res.json();

          const countryMap = {};
          data.forEach(country => {
            countryMap[country.cca3] = country.name.official;   // here, official is taking the official name of a country, cca3 means CAD/USD/etc
          });

          setCountries(data);
          setCodeToNameMap(countryMap);

        } catch (error) {
          console.error('Failed to fetch country data:', error);
        }
      };

      fetchCountries();
    }, []);

  // show countries
    const handleCountryA = () => {
      setCountryA(true);
      setCountryI(false);
    };

    const handleCountryI = () => {
      setCountryA(false);
      setCountryI(true);
    };

  return (
    <div className='appcontainer'>
      <h1>
        Neighboring Countries
      </h1>

      <div>
        <button onClick = {handleCountryA}>
          Neighbours Starting with A
        </button>

        <button onClick = {handleCountryI}>
          Neighbours Starting with I
        </button>
      </div>

      {displayA && <NeighboursA countries={countries} countryMap={codeToNameMap} />}  {/* if variable is truthy, render countries and countryMap */}
      {displayI && <NeighboursI countries={countries} countryMap={codeToNameMap} />}
    </div>
  )
}

export default App
