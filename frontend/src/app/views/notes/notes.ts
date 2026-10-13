import { Component, inject } from '@angular/core';
import { DefaultService } from '../../../api';
import { toSignal } from '@angular/core/rxjs-interop';

@Component({
  selector: 'app-notes',
  imports: [],
  templateUrl: './notes.html',
  styleUrl: './notes.css',
})
export class Notes {
  defaultService = inject(DefaultService);

  notes = toSignal(this.defaultService.readNotesNotesGet());
}
