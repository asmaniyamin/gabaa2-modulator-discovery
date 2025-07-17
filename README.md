# Identifying Novel Anxiolytic Drugs for Selective Modulation of the α2 Subunit of GABA-A

This project was created for Stanford's CS229 course - "Machine Learning". It demonstrates a prototype application of existing machine learning algorithms for processing billion-scale molecular datasets, specifically in the context of drug discovery.

The focus of this pipeline is to identify selective modulators of the GABA-A receptor's α2 subunit, which plays a critical role in anxiolytic (anti-anxiety) effects. We perform massive-scale filtering of the Enamine REAL library, combined with processing of known compounds, to enhance discovery of selective GABA-A-α2 ligands.

## Paper

The associated paper can be found in [`GABA-a2-Modulatory-Discovery.pdf`](GABA-a2-Modulatory-Discovery.pdf).

## Data Access

The data files missing can be downloaded here:

**[bbb_filtering/data/data_parquet_bbb.zip (200 MB)](https://drive.google.com/file/d/1I-0GAGsMBrw9sOcrRD9X4ML55QpI7mfX/view?usp=sharing)**

## Project Structure

```
bbb_filtering/           # Scripts and data for BBB filtering
├── fingerprints_BBB/    # Molecular fingerprints for BBB classification
├── data/                # Parquet and auxiliary files used in filtering
...

mpnn/                    # Molecular Selectivity Prediction with MPNN
├── src/                 # Code for the MPNN pipeline
├── data/                # Raw and processed data
...
```
