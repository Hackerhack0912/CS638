from datetime import datetime
import re
import csv
import sys
import py_entitymatching as em


def main():
    # should use utf-8 encoding to prevent errors of decoding in python3
    # I changed the column name in tableA.csv so it matches the names of the output csv
    # then I can directly reorder the columns by their names
    with open('tableG.csv', "r", encoding='utf-8') as inFile, open('tableH.csv', "w", encoding='utf-8') as outFile:
        # new column ordering for output csv
        outputFields = ['_id', 'ltable_id', 'rtable_id','title_affine_score','title_lev_dist_score','title_lev_sim_score','title_jaro_score','title_jaro_winkler_score','title_needleman_wunsch_score','title_smith_waterman_score','title_jaccard_score','title_cosine_score','title_overlap_coeff_score', 'title_dice_score','title_monge_elkan_score','author_affine_score','author_lev_dist_score','author_lev_sim_score','author_jaro_score','author_jaro_winkler_score','author_needleman_wunsch_score','author_smith_waterman_score','author_jaccard_score','author_cosine_score','author_overlap_coeff_score', 'author_dice_score','author_monge_elkan_score','publisher_affine_score','publisher_lev_dist_score','publisher_lev_sim_score','publisher_jaro_score','publisher_jaro_winkler_score','publisher_needleman_wunsch_score','publisher_smith_waterman_score','publisher_jaccard_score','publisher_cosine_score','publisher_overlap_coeff_score', 'publisher_dice_score','publisher_monge_elkan_score','year_rel_diff','year_abs_norm','month_rel_diff','month_abs_norm','pages_rel_diff','pages_abs_norm','gold']

        writer = csv.DictWriter(outFile, fieldnames=outputFields)
        q = 3
        # write first row which is the header
        writer.writeheader()
        for row in csv.DictReader(inFile):
            lTitle =  row['ltable_title']
            lAuthors = row['ltable_authors']
            lPublisher = row['ltable_publisher']
            lYear = row['ltable_publishedYear']
            lMonth = row['ltable_publishedMonth']
            lPages = row['ltable_pages']

            rTitle =  row['rtable_title']
            rAuthors = row['rtable_authors']
            rPublisher = row['rtable_publisher']
            rYear = row['rtable_publishedYear']
            rMonth = row['rtable_publishedMonth']
            rPages = row['rtable_pages']
           	
            # title
            s1 = lTitle
            s2 = rTitle
            title_affine_score = em.affine(s1, s2)
            #title_hamming_dist_score = em.hamming_dist(s1, s2)
            #title_hamming_sim_score = em.hamming_sim(s1, s2)
            title_lev_dist_score = em.lev_dist(s1, s2)
            title_lev_sim_score = em.lev_sim(s1, s2)
            title_jaro_score = em.jaro(s1, s2)
            title_jaro_winkler_score = em.jaro_winkler(s1, s2)
            title_needleman_wunsch_score = em.needleman_wunsch(s1, s2)
            title_smith_waterman_score = em.smith_waterman(s1, s2)            
            arr1 = em.tok_qgram(s1,q)
            arr2 = em.tok_qgram(s2,q)
            title_jaccard_score = em.jaccard(arr1, arr2)
            title_cosine_score = em.cosine(arr1, arr2)
            title_overlap_coeff_score = em.overlap_coeff(arr1, arr2)
            title_dice_score = em.dice(arr1, arr2)
            title_monge_elkan_score = em.monge_elkan(arr1, arr2)

            # author
            s1 = lAuthors
            s2 = rAuthors
            author_affine_score = em.affine(s1, s2)
            #author_hamming_dist_score = em.hamming_dist(s1, s2)
            #author_hamming_sim_score = em.hamming_sim(s1, s2)
            author_lev_dist_score = em.lev_dist(s1, s2)
            author_lev_sim_score = em.lev_sim(s1, s2)
            author_jaro_score = em.jaro(s1, s2)
            author_jaro_winkler_score = em.jaro_winkler(s1, s2)
            author_needleman_wunsch_score = em.needleman_wunsch(s1, s2)
            author_smith_waterman_score = em.smith_waterman(s1, s2)            
            arr1 = em.tok_qgram(s1,q)
            arr2 = em.tok_qgram(s2,q)
            author_jaccard_score = em.jaccard(arr1, arr2)
            author_cosine_score = em.cosine(arr1, arr2)
            author_overlap_coeff_score = em.overlap_coeff(arr1, arr2)
            author_dice_score = em.dice(arr1, arr2)
            author_monge_elkan_score = em.monge_elkan(arr1, arr2)

            # publisher
            s1 = lPublisher
            s2 = rPublisher
            publisher_affine_score = em.affine(s1, s2)
            #publisher_hamming_dist_score = em.hamming_dist(s1, s2)
            #publisher_hamming_sim_score = em.hamming_sim(s1, s2)
            publisher_lev_dist_score = em.lev_dist(s1, s2)
            publisher_lev_sim_score = em.lev_sim(s1, s2)
            publisher_jaro_score = em.jaro(s1, s2)
            publisher_jaro_winkler_score = em.jaro_winkler(s1, s2)
            publisher_needleman_wunsch_score = em.needleman_wunsch(s1, s2)
            publisher_smith_waterman_score = em.smith_waterman(s1, s2)            
            arr1 = em.tok_qgram(s1,q)
            arr2 = em.tok_qgram(s2,q)
            publisher_jaccard_score = em.jaccard(arr1, arr2)
            publisher_cosine_score = em.cosine(arr1, arr2)
            publisher_overlap_coeff_score = em.overlap_coeff(arr1, arr2)
            publisher_dice_score = em.dice(arr1, arr2)
            publisher_monge_elkan_score = em.monge_elkan(arr1, arr2)

            # year, month, pages
            print([lYear,lMonth,lPages])
            print([rYear,rMonth,rPages])
            year_rel_diff = em.rel_diff(int(lYear), int(rYear))
            year_abs_norm = em.abs_norm(int(lYear), int(rYear))
            month_rel_diff = em.rel_diff(int(lMonth), int(rMonth))
            month_abs_norm = em.abs_norm(int(lMonth), int(rMonth))
            pages_rel_diff = em.rel_diff(int(lPages), int(rPages))
            pages_abs_norm = em.abs_norm(int(lPages), int(rPages))

            writer.writerow({  '_id': row['_id'], 'ltable_id': row['ltable_id'], 'rtable_id': row['rtable_id'], 'title_affine_score': title_affine_score, 'title_lev_dist_score': title_lev_dist_score, 'title_lev_sim_score': title_lev_sim_score, 'title_jaro_score': title_jaro_score, 'title_jaro_winkler_score': title_jaro_winkler_score, 'title_needleman_wunsch_score': title_needleman_wunsch_score, 'title_smith_waterman_score': title_smith_waterman_score, 'title_jaccard_score': title_jaccard_score, 'title_cosine_score': title_cosine_score, 'title_overlap_coeff_score': title_overlap_coeff_score, 'title_dice_score': title_dice_score, 'title_monge_elkan_score': title_monge_elkan_score, 'author_affine_score': author_affine_score,  'author_lev_dist_score': author_lev_dist_score, 'author_lev_sim_score': author_lev_sim_score, 'author_jaro_score': author_jaro_score, 'author_jaro_winkler_score':author_jaro_winkler_score, 'author_needleman_wunsch_score':author_needleman_wunsch_score, 'author_smith_waterman_score':author_smith_waterman_score, 'author_jaccard_score':author_jaccard_score, 'author_cosine_score':author_cosine_score, 'author_overlap_coeff_score': author_overlap_coeff_score, 'author_dice_score': author_dice_score, 'author_monge_elkan_score':author_monge_elkan_score, 'publisher_affine_score': publisher_affine_score, 'publisher_lev_dist_score': publisher_lev_dist_score, 'publisher_lev_sim_score': publisher_lev_sim_score, 'publisher_jaro_score': publisher_jaro_score, 'publisher_jaro_winkler_score': publisher_jaro_winkler_score, 'publisher_needleman_wunsch_score': publisher_needleman_wunsch_score, 'publisher_smith_waterman_score':publisher_smith_waterman_score, 'publisher_jaccard_score':publisher_jaccard_score, 'publisher_cosine_score':publisher_cosine_score, 'publisher_overlap_coeff_score':publisher_overlap_coeff_score, 'publisher_dice_score':publisher_dice_score, 'publisher_monge_elkan_score': publisher_monge_elkan_score, 'year_rel_diff': year_rel_diff, 'year_abs_norm': year_abs_norm, 'month_rel_diff': month_rel_diff, 'month_abs_norm':month_abs_norm, 'pages_rel_diff': pages_rel_diff, 'pages_abs_norm': pages_abs_norm, 'gold': row['gold']         })

    inFile.close()
    outFile.close()

main()
