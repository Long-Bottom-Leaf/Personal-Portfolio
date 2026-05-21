export const mapFlightData = (
  flights,
  airlines,
  airports,
  gates
) => {
  return flights.map((flight) => {
    const airline = airlines.find(
      (a) => a.id === flight.airlineId
    );

    const departureAirport = airports.find(
      (a) => a.id === flight.departureAirportId
    );

    const gate = gates.find(
      (g) => g.id === flight.gateId
    );

    return {
      ...flight,
      airlineName: airline?.name || "Unknown",
      departureCode: departureAirport?.code || "N/A",
      gateNumber: gate?.gateNumber || "TBD",
    };
  });
};