covid_variant('Mu').
covid_variant('Delta').
covid_variant('Covid-19'). %This is the original strain

%['Nausea','Gonnerrea'].
%symptom(['Nausea','Gonnerea','Rich']). % This is called a list

have_mu(Temperature,X):-Temperature>=39.5,compare_list(X,['Nausea','Short of Breath','Body Ache']). %symptoms of mu variant, this works
have_delta(Temperature,X):- Temperature>=39.5,compare_list(X,['Runny Nose','Headache','Sore Throat','Fever']).
have_covid(Temperature,X):-Temperature>=39.5,compare_list(X,['Cough','Tiredness','Loss of taste or smell']).

covid_diag(Temperature,Symp,Diag):- have_mu(Temperature,Symp) -> Diag is 1;
                                    have_delta(Temperature,Symp)-> Diag is 2;
                                    have_covid(Temperature,Symp) -> Diag is 3; Diag is 4.



blood_pressure_warn(Sys,Dias,Warn):- Sys<90,Dias<60 -> Warn is 1; % 1 for low, 2 for normal and  3 for high
                                     Sys>=130,Dias>=80 -> Warn is 3;
                                     Warn is 2.
%This works

severity(Temp,NumSym,Severity):- NumSym>=3;Temp>39.5 -> Severity is 1; Severity is 2.
                           % 2 if non-severe, 1 if otherwise
                           %39.5 is a high fever
%this works


compare_list([L1Head|L1Tail], List2):-
   member(L1Head, List2);
   compare_list(L1Tail, List2).


%compares a list
