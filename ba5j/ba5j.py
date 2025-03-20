from Bio import SeqIO, Align
from Bio.Align import substitution_matrices
import sys

# load the fasta file into a list of tuples like (id, sequence)
def load_sequences(input):
    sequences = []
    for record in SeqIO.parse(input, "fasta"):
        sequences.append((record.id, record.seq))
    return sequences

# Check if the sequences only contain valid characters
def verify_sequence(sequence):
    matrix = substitution_matrices.load("BLOSUM62")
    valid_characters = matrix.alphabet

    if set(sequence).issubset(set(valid_characters)):
        return True
    else:
        return False


if __name__ == "__main__":

    # Generate aligner
    aligner = Align.PairwiseAligner()
    # set aligner parameters
    aligner.mode = "global"
    aligner.substitution_matrix = substitution_matrices.load("BLOSUM62")
    aligner.open_gap_score = -11
    aligner.extend_gap_score = -1

    # Load sequences, verify them, generate alignmets and get the score
    input = sys.argv[1]
    output = sys.argv[2]
    sequences = load_sequences(input)

    with open(output, "w") as output:
        target_id, target_seq = sequences[0] # target sequence for the alignments
        # check if the target is valid
        if verify_sequence(target_seq) == False:
            print("Target: {} contains an invalid character".format(target_id))
        else:
            for sequence in sequences[1:]:
                id, seq = sequence
                # check if the query is valid
                if verify_sequence(seq) == False:
                    print("Query: {} contains an invalid character".format(id))
                else:
                    alignments = aligner.align(target_seq, seq) # sequence is used as query

                    output.write(f">{target_id}\n{alignments[0][0]}\n>{id}\n{alignments[0][1]}\n")  
                    print("Number of alignments: {} and score: {}".format(len(alignments), alignments.score))

