import './Neighbours.css';

const NeighboursA = ({countries, countryMap}) => {
    const filterCountries = countries.filter(country => {           // goes through the list and filters based on given filter parameters
        if (!country.borders) return false;                         // if country has no neighbours, return false

        const neighbourNames = country.borders.map(code => countryMap[code] || " ");    // takes the border code and converts to country name using countryMap
        return neighbourNames.some(name => name.startsWith('A'));                       // returns each country that starts with A
    });

  return (
    <div>
        {filterCountries.map((country) => (       // map through each filtered country
            <div key={country.cca3}>                {/* give each country a unique key using cca3 */}
            <h2>{country.name.official}</h2>      {/* display official country name */}

            <p>
                <strong>Capital:</strong> {country.capital?.[0] || 'No capital to display'}
            </p>                                  {/* access the first capital, if none exist, show message */}

            <img
                src={country.flags.svg}
                alt={`Flag of ${country.name.official}`}
                width="100"
            />                                     {/* display the country's flag */}

            <p><strong>Neighbors:</strong></p>
            <ul>
                {country.borders?.map(code => (
                <li key={code}>{countryMap[code]}</li>
                ))}                                  {/* goes through each country.borders and creates a list element, if there is no border it skips */}
            </ul>
            </div>
        ))}
    </div>
  )
}

export default NeighboursA