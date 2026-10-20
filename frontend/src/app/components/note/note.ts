import { Component, input } from '@angular/core';

@Component({
  selector: 'app-note',
  imports: [],
  templateUrl: './note.html',
  styleUrl: './note.css',
})
export class Note {
  readonly title = input();
  readonly content = input();
}
