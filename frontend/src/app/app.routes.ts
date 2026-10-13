import { Routes } from '@angular/router';
import { Home } from './views/home/home';
import { Notes } from './views/notes/notes';

export const routes: Routes = [
    {
        path: '',
        component: Home
    },
    {
        path: 'notes',
        component: Notes
    }
];
