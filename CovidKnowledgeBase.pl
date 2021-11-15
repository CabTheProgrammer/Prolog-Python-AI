covid_variant('Mu').
covid_variant('Delta').
covid_variant('Covid-19'). %This is the original strain

%['Nausea','Gonnerrea'].
%
symptom(['Nausea','Gonnerea','Rich']). % This is called a list

have_mu(Temperature,X):-Temperature>=120,member(X,['Nausea','Gonnerea','Rich']). %symptoms of mu variant
%blood_pressure_warn(Sys,Dias):-.



severity(NumSym,Severity):- NumSym>=3 -> Severity is 1;
                            NumSym=<2 -> Severity is 2.
                            %nl,write(Severity).
