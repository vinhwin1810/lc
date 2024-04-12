CREATE TABLE Genes (
    gene_id INTEGER PRIMARY KEY,
    gene_name TEXT NOT NULL,
    chromosome_id INTEGER,
    start_position INTEGER,
    end_position INTEGER,
    FOREIGN KEY (chromosome_id) REFERENCES Chromosomes(chromosome_id)
);

CREATE Chromosomes(
    chromosome_id INTEGER PRIMARY KEY,
    chromosome_name TEXT NOT NULL
);

CREATE TABLE Proteins(
    protein_id INTEGER PRIMARY KEY,
    protein_name TEXT NOT NULL,
    gene_id INTEGER,
    FOREIGN KEY (gene_id) REFERENCES Genes(gene_id)
);

CREATE TABLE Experiments(
    experiment_id INTEGER PRIMARY KEY,
    experiment_name TEXT NOT NULL,
    researcher_id INTEGER,
    date_conducted DATE,
    FOREIGN KEY (researcher_id) REFERENCES Researchers(researcher_id)
);

CREATE TABLE ResearchPublications(
    publication_id INTEGER PRIMARY KEY,
    publication_title TEXT NOT NULL,
    publication_date DATE,
    experiment_id INTEGER,
    FOREIGN KEY (experiment_id) REFERENCES Experiments(experiment_id)
);

CREATE TABLE Researchers(
    researcher_id INTEGER PRIMARY KEY,
    researcher_name TEXT NOT NULL
)