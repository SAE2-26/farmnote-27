import { Component, computed, effect, inject, signal } from '@angular/core';
import { DefaultService } from '../../../api';
import { toSignal } from '@angular/core/rxjs-interop';
import { Note } from '../../components/note/note';

@Component({
  selector: 'app-notes',
  imports: [Note],
  templateUrl: './notes.html',
  styleUrl: './notes.css',
})
export class Notes {
  defaultService = inject(DefaultService);

  notes = toSignal(this.defaultService.readNotesNotesGet());

}
