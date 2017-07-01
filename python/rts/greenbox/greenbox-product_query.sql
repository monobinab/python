select
productId,--ksn, catentry_id, sin, child_description, parent_partnumber, imaitemid, uid
brand,
title,
regPrice,--regular_price
curPrice,--current_price
--imgUrl,
--clickUrl,
mapV,--mapval
star,--isenergystar
recType,--product_type, item_type, sywr_item_type, disptags_sywitemtype, offertype, upctype
quantity,--dfltquantity
mapIndicator,--instock_indicator
regionalPricingEligible,--isrgnpriceelig
--regionalPriced,
--seoClickUrl,
--savings,
freeShipping,--isshipelig, shipping_handling_fee
defaultFulfillment,--ffm_fulfilledby
variant
from
smith_sears_kmart_product_content
;

offer_id, sites, ksn, ffm_source, sold_by, height, length, width, wg_code, product_type, hazmat_code, unit_cost, factory_pack, upc, item_type, ssin, weight, vendor_pack, brand_name, no_spuc, web_exclusive, km_sres_ind, is_recalled, amazon_prc_elig, is_sam, is_rim, is_installable, purchase_unavail, markfordelete, view_only, actual_start_dt, purchase_status, sywr_item_type, km_delivery, rim_status, configure_tech_flag, rsos_ind, is_ltl_override, offline_price_threshold, positive_margin_threshold, negative_margin_threshold, warn_prc_threshold, price_alert_email, prc_alert_exclusion_date, prc_alert_reset_val, street_date, km_pr_elig, flex_spend_elig, amazon_price_elig, amazon_price_elig_raw, amazon_price_elig_rsn, mail_elig, rgn_prc_elig, prc_alert_active, pos_margin_thrshld, excl_price_thrshld, sku_sopt, max_ship_elig, spin_prpdt, active_start_dt, disp_elig, disp_elig_rsn, inactive_enddt, inactive_startdt, ffm_chnl, ffm_chnlrsn, ffm_wrhslcn, ffm_wrhslcnrsn, hfm_ind, hfm_ind_rsn, comm_inv, comm_inv_rsn, is_mailable, is_mailable_rsn, max_shp_elig, max_shp_elig_rgn, sfs_elig, sfs_elig_rsn, spu_elig, spu_elig_rsn, sres_elig, sres_elig_rsn, ndd_elig, ndd_elig_rsn, sts, sts_rsn, is_ship_elig, shp_elig_rsn, is_delvr_elig, delvr_elig_rsn, is_chth_excln, chth_excln_rsn, def_ffm_opt, ffm_by, ft_pgrmtype, search_upc, search_ksn, created_by, createdts, modified_by, modifiedts, tmstmp, jobrunts


 or smith_sears_kmart_product_content

catentry_id, child_partnumber, child_description, markfordelete, parent_catentry_id, parent_partnumber, item_store, sin, item_type, vendor_id, seller_id, seller_name, brand, commission_sears_rate, commission_mygofer_rate, commission_default_rate, item_name, manufacturer_name, model_number, shipping_handling_fee, minimum_shipping_rate, view_only, variant, product_recalled, unit_cost, vendor_packid, vendor_stock_number, web_exclusive, weight, length, width, height, upc, ksn, product_meta_createdts, product_meta_modifiedts, product_meta_createdts_year, product_meta_createdts_month, product_meta_createdts_day, product_meta_createdts_hour, product_meta_createdts_week_number, product_meta_modifiedts_year, product_meta_modifiedts_month, product_meta_modifiedts_day, product_meta_modifiedts_hour, product_meta_modifiedts_week_number, content_ssin, itm_nbr, disptags_sywitemtype

offer_id, sites, offertype, isuvd, isautomotive, iskmartprelig, brand, defattr, modelno, mapval, mapthrshld, isexcptval, ismbrprc, isamzprcelig, ishotbuy, isupp, isprcalrtexcln, isdiscntexcld, mfrpartno, seasoncode, mapvalmode, mapmsg, mapdesc, isrgnpriceelig, isprcalrtclr, warnprcthrshld, offlnprcthrshld, prcalrtemail, prcalrtexcldt, condition_status, condition_comments, condition_img_alt, condition_img_height, condition_img_src, condition_img_title, condition_img_width, alternateimg, swatchimage, mainimage, height, length, width, taxcode, maxshipelig, minrate, soptdays, issywrmaxshipelig, isshipalone, isflatrateship, handlingfee, weight, shipsurcharge, issimielig, isgroundonly, htccode, presell_qty, presell_streetdt, isdeliveryelig, ischeetahexclusion, isdonotemailme, islayawayelig, issfselig, isshipelig, issreselig, isstselig, stschannel, iswebexcl, isspuelig, vendordunsno, ffm_fulfilledby, ffm_soldby, ffm_channel, warehouse_location, replenishment_internalrimsts, replenishment_futureactivestartdate, replenishment_purchasests, unitcost, replenishment_vendorpackid, replenishment_cancarrygrp, replenishment_coreitemflag, replenishment_rsosindicator, replenishment_isrecalled, isalcohol, isfreezing, isperishable, isrefrigeration, istobacco, markfordelete, operational_sites, firstonlinedt, isdispelig, inactive_startdt, inactive_enddt, isreserveit, ksn, spinid, upctype, upc, imaitemid, imaclasscontrolpid, vendorstockno, isdeliverysetupelig, istire, isclicktotalkelig, lpvoiceid, lpchatid, isenergystar, viewonly, issearsexclusive, ispricefreqmodel, ispremshipelig, isexpresscheckoutelig, isegiftelig, isgftwrapelig, isinstallable, ishaulawayelig, warrantyindicator, isoutletitem, dfltquantity, sywitemtype, createdts, sellerid, pgrmtype, divitem, ssin, uid, sears_invthreshold, kmart_invthreshold, actual_start_dt, is_sam, is_rim, wg_code, unit_cost, prc_alert_active, child_description, vendor_id, seller_id, seller_name, variant, sale_price, regular_price, current_price, instock_indicator, manufacturer_name, sale_end_date, online_date, backord, backordrsvd, onhand, onhandrsvd, presellonhand, presellonhandrsvd, readytopick, layawayrsvd, location_type, location_name, bu_nm, vbs_no, vbs_nm, div_no, div_nm, ln_no, ln_ds, sbl_no, sbl_ds, cls_no, cls_ds, replenishment_hfmind, marketplace_programtype, marketplace_seller_id, marketplace_seller_name, ffmelig_cheetah, ffmelig_vres, ffmelig_cres, ffmelig_dres, parentid, amazon_price_elig, street_date, parent_partnumber, vendor_name, itm_nbr, is_exceptional_value_gp, is_clearance_ind, item_store, location_id, shipavail, pickupavail, deliveryavail, ffm_calcode, ffm_spinvendorid, search_spinid, ffmelig_rr, ffmelig_cdfc, ffmelig_dart, isnddinelig, ffmelig_xsres, replenishment_flowtype, legal_usdottype, sywrdmelig, marketplace_sywrdmelig)


select
ksn, 
--catentry_id, 
--sin, 
ssin,
child_description, 
parent_partnumber, 
imaitemid, 
mainimage,
uid
brand,
--title,
condition_img_title,
regular_price,
current_price,
mapval,
isenergystar,
--product_type, 
--item_type, 
--sywr_item_type, 
--disptags_sywitemtype, 
offertype, upctype,
dfltquantity,
instock_indicator,
isrgnpriceelig,
isshipelig, 
--shipping_handling_fee,
shipsurcharge,
handlingfee,
ffm_fulfilledby,
variant
from
smith_sears_kmart_product_content
;

select count(*) from smith_sears_kmart_product_content;--125024221
select count(*) from smith_content_offer;--              114586077
														 110607843

create table greenbox_product_desc (
ksn string, 
ssin string,
child_description string, 
parent_partnumber string, 
imaitemid string, 
mainimage string,
uid string,
brand string,
condition_img_title string,
regular_price string,
current_price string,
mapval string,
isenergystar string,
offertype string, 
upctype string,
dfltquantity string,
instock_indicator string,
isrgnpriceelig string,
isshipelig string, 
shipsurcharge string,
handlingfee string,
ffm_fulfilledby string,
variant string
)
row format delimited
fields terminated by '|'
lines terminated by '\n'
stored as textfile
;

insert into table greenbox_product_desc
select
ksn, 
ssin,
child_description, 
parent_partnumber, 
imaitemid, 
mainimage,
uid,
brand,
condition_img_title,
regular_price,
current_price,
mapval,
isenergystar,
offertype, 
upctype,
dfltquantity,
instock_indicator,
isrgnpriceelig,
isshipelig, 
shipsurcharge,
handlingfee,
ffm_fulfilledby,
variant
from
smith_sears_kmart_product_content
;


