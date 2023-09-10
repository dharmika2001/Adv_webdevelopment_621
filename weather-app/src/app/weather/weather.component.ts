import { Component, OnInit } from '@angular/core';
import { FormBuilder, FormGroup } from '@angular/forms';
import { ApixuService } from "../apixu.service";



@Component({
  selector: 'app-weather',
  templateUrl: './weather.component.html',
  styleUrls: ['./weather.component.css']
})
export class WeatherComponent implements OnInit {
  weatherSearchForm: FormGroup;
  weatherData: any; 

  constructor(private formBuilder: FormBuilder, private apixuService: ApixuService) {
    this.weatherSearchForm = this.formBuilder.group({
      location: [''] 
    });
  }

  ngOnInit() {}

  sendToAPIXU() {
    const location = this.weatherSearchForm.value.location;
    this.apixuService.getWeather(location).subscribe((data: any) => {
      this.weatherData = data;
    });
  }
}
