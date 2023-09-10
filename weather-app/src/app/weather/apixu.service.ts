import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';

@Injectable({
  providedIn: 'root'
})
export class ApixuService {
  private apiKey: string = '0c3e94f5b8e04180ba1e27707d177eea';
  private baseUrl: string = 'http://api.weatherstack.com/';

  constructor(private http: HttpClient) {}

  getWeather(location: string) { // Provide a type annotation for the 'location' parameter
    const apiUrl = `${this.baseUrl}current?access_key=${this.apiKey}&query=${location}`;
    return this.http.get(apiUrl);
  }
}
