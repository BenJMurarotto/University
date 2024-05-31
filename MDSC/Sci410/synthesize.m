function [proteinstring] = synthesize(codonstring)
%synthesize(codonstring) = [proteinstring]
%This function takes a codon string of DNA eg 'CCCAUCUGACAACG' 
%and converts it into its corresponding amino acid
inputlen = length(codonstring);
upperstring = upper(codonstring);
proteinstring = '';

codonref = containers.Map( ...
        {'UUU', 'UUC', 'UUA', 'UUG', 'CUU', 'CUC', 'CUA', 'CUG', 'AUU', 'AUC', 'AUA', 'AUG', 'GUU', 'GUC', 'GUA', 'GUG', ...
         'UCU', 'UCC', 'UCA', 'UCG', 'CCU', 'CCC', 'CCA', 'CCG', 'ACU', 'ACC', 'ACA', 'ACG', 'GCU', 'GCC', 'GCA', 'GCG', ...
         'UAU', 'UAC', 'UAA', 'UAG', 'CAU', 'CAC', 'CAA', 'CAG', 'AAU', 'AAC', 'AAA', 'AAG', 'GAU', 'GAC', 'GAA', 'GAG', ...
         'UGU', 'UGC', 'UGA', 'UGG', 'CGU', 'CGC', 'CGA', 'CGG', 'AGU', 'AGC', 'AGA', 'AGG', 'GGU', 'GGC', 'GGA', 'GGG'}, ...
        {'F', 'F', 'L', 'L', 'L', 'L', 'L', 'L', 'I', 'I', 'I', 'M', 'V', 'V', 'V', 'V', ...
         'S', 'S', 'S', 'S', 'P', 'P', 'P', 'P', 'T', 'T', 'T', 'T', 'A', 'A', 'A', 'A', ...
         'Y', 'Y', 'Stop', 'Stop', 'H', 'H', 'Q', 'Q', 'N', 'N', 'K', 'K', 'D', 'D', 'E', 'E', ...
         'C', 'C', 'Stop', 'W', 'R', 'R', 'R', 'R', 'S', 'S', 'R', 'R', 'G', 'G', 'G', 'G'});

for i = 1:3:inputlen
    codon = upperstring(i:i+2);
    aa = codonref(codon);
    if strcmp(aa, 'Stop') % Checking for stop codon
        break;
    end
    proteinstring = [proteinstring, aa];
end
end