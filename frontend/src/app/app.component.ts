import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { HttpClient, HttpClientModule } from '@angular/common/http';

@Component({
  selector: 'app-root',
  standalone: true,
  imports: [
    CommonModule,
    FormsModule,
    HttpClientModule
  ],
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {

  question = '';

  loading = false;

  response: any = null;

  constructor(private http: HttpClient) {}

  askQuestion() {

    if (!this.question.trim()) {
      return;
    }

    this.loading = true;

    this.http.get(
      `http://localhost:8000/rag-ask?question=${encodeURIComponent(this.question)}`
    ).subscribe({
      next: (res) => {
        this.response = res;
        this.loading = false;
      },
      error: (err) => {
        console.error(err);
        this.loading = false;
      }
    });
  }
}