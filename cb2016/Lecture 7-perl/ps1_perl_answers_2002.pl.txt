#!/usr/bin/perl

###########################
#### The Central Dogma ####
###########################

### Genome
$DNA_seq = "ATGACCCTACTAGATCATCTATGATAGCTCAT"; # DNA sequence to translate

### Transcription
$RNA_seq = $DNA_seq; # copies DNA sequence
$RNA_seq =~ s/T/U/gi; # replaces T's with U's (g=global, i=case insensitive)
print "$RNA_seq\n"; # prints the RNA sequence

### Translation
$position = 0; # start position
while (substr $RNA_seq,$position,3) { # executes loop until end of string reached
	$codon = substr $RNA_seq,$position,3; # defines the codon
	print translate_codon($codon); # calls the translate codon subroutine and prints result
	$position = $position + 3; # moves ahead 3 bases
}

sub translate_codon { # subroutine to translate codons
	if ($_[0] =~ /GC./i) {return Ala;} # matches to "GC then any letter" returns Ala
	if ($_[0] =~ /UGC|UGU/i) {return Cys;} # matches to UGC or UGU returns Cys
	if ($_[0] =~ /GAC|GAU/i) {return Asp;} # etc...
	if ($_[0] =~ /GAA|GAG/i) {return Glu;}
	if ($_[0] =~ /UUC|UUU/i) {return Phe;}
	if ($_[0] =~ /GG./i) {return Gly;}
	if ($_[0] =~ /CAC|CAU/i) {return His;}
	if ($_[0] =~ /AUA|AUC|AUU/i) {return Ile;}
	if ($_[0] =~ /AAA|AAG/i) {return Lys;}
	if ($_[0] =~ /UUA|UUG|CU./i) {return Leu;}
	if ($_[0] =~ /AUG/i) {return Met;}
	if ($_[0] =~ /AAC|AAU/i) {return Asn;}
	if ($_[0] =~ /CC./i) {return Pro;}
	if ($_[0] =~ /CAA|CAG/i) {return Gln;}
	if ($_[0] =~ /AGA|AGG|CG./i) {return Arg;}
	if ($_[0] =~ /AGC|AGU|UC./i) {return Ser;}
	if ($_[0] =~ /AC./i) {return Thr;}
	if ($_[0] =~ /GU./i) {return Val;}
	if ($_[0] =~ /UGG/i) {return Trp;}
	if ($_[0] =~ /UAC|UAU/i) {return Tyr;}
	if ($_[0] =~ /UAA|UGA|UAG/i) {return "***";} # Stop codons
}

