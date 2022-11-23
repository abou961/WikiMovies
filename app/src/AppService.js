class ApiService {

  static getMovie = async (idMovie) => {
    const response = await fetch(
        `/movie?id=${idMovie}`
        );
    return response.json();
  }

  static getSeries = async (idSeries) => {
    const response = await fetch(
        `/series?id=${idSeries}`
        );
    return response.json();
  }

  static getPerson = async (idPerson) => {
    const response = await fetch(
        `/person?id=${idPerson}`
        );
    return response.json();
  }

  static getSearchFilm = async (stringSearch) => {
    const response = await fetch(
        `/search?input=${stringSearch}`
        );
    return response.json();
  }
};

export default ApiService;