import glob, os

from .exac_parser import load_data
import biothings.dataload.uploader as uploader
from dataload.uploader import SnpeffPostUpdateUploader

class ExacBaseUploader(SnpeffPostUpdateUploader):

    id_type = 'observed'

    @classmethod
    def get_mapping(klass):
        mapping = {
            "exac": {
                "properties": {
                    "chrom": {
                        "type": "string",
                        "analyzer": "string_lowercase"
                    },
                    "pos": {
                        "type": "long"
                    },
                    "ref": {
                        "type": "string",
                        "analyzer": "string_lowercase"
                    },
                    "alt": {
                        "type": "string",
                        "analyzer": "string_lowercase"
                    },
                    "alleles": {
                        "type": "string",
                        "analyzer": "string_lowercase"
                    },
                    "type": {
                        "type": "string",
                        "analyzer": "string_lowercase"
                    },
                    "qual": {
                        "type": "float"
                    },
                    "filter": {
                        "type": "string",
                        "analyzer": "string_lowercase"
                    },
                    "ac": {
                        "properties": {
                            "ac": {
                                "type": "integer"
                            },
                            "ac_afr": {
                                "type": "integer"
                            },
                            "ac_amr": {
                                "type": "integer"
                            },
                            "ac_adj": {
                                "type": "integer"
                            },
                            "ac_eas": {
                                "type": "integer"
                            },
                            "ac_fin": {
                                "type": "integer"
                            },
                            "ac_nfe": {
                                "type": "integer"
                            },
                            "ac_oth": {
                                "type": "integer"
                            },
                            "ac_sas": {
                                "type": "integer"
                            },
                            "ac_male": {
                                "type": "integer"
                            },
                            "ac_female": {
                                "type": "integer"
                            }
                        }
                    },
                    "af": {
                        "type": "float"
                    },
                    "an": {
                        "properties": {
                            "an": {
                                "type": "integer"
                            },
                            "an_afr": {
                                "type": "integer"
                            },
                            "an_amr": {
                                "type": "integer"
                            },
                            "an_adj": {
                                "type": "integer"
                            },
                            "an_eas": {
                                "type": "integer"
                            },
                            "an_fin": {
                                "type": "integer"
                            },
                            "an_nfe": {
                                "type": "integer"
                            },
                            "an_oth": {
                                "type": "integer"
                            },
                            "an_sas": {
                                "type": "integer"
                            },
                            "an_female": {
                                "type": "integer"
                            },
                            "an_male": {
                                "type": "integer"
                            }
                        }
                    },
                    "baseqranksum": {
                        "type": "float"
                    },
                    "clippingranksum": {
                        "type": "float"
                    },
                    "fs": {
                        "type": "float"
                    },
                    "dp": {
                        "type": "long"
                    },
                    "het": {
                        "properties": {
                            "het_afr": {
                                "type": "integer"
                            },
                            "het_amr": {
                                "type": "integer"
                            },
                            "het_eas": {
                                "type": "integer"
                            },
                            "het_fin": {
                                "type": "integer"
                            },
                            "het_nfe": {
                                "type": "integer"
                            },
                            "het_oth": {
                                "type": "integer"
                            },
                            "het_sas": {
                                "type": "integer"
                            },
                            "ac_het": {
                                "type": "integer"
                            }
                        }
                    },
                    "hom": {
                        "properties": {
                            "hom_afr": {
                                "type": "integer"
                            },
                            "hom_amr": {
                                "type": "integer"
                            },
                            "hom_eas": {
                                "type": "integer"
                            },
                            "hom_fin": {
                                "type": "integer"
                            },
                            "hom_nfe": {
                                "type": "integer"
                            },
                            "hom_oth": {
                                "type": "integer"
                            },
                            "hom_sas": {
                                "type": "integer"
                            },
                            "ac_hom": {
                                "type": "integer"
                            }
                        }
                    },
                    "inbreedingcoeff": {
                        "type": "float"
                    },
                    "mq": {
                        "properties": {
                            "mq": {
                                "type": "float"
                            },
                            "mq0": {
                                "type": "integer"
                            },
                            "mqranksum": {
                                "type": "float"
                            }
                        }
                    },
                    "ncc": {
                        "type": "long"
                    },
                    "qd": {
                        "type": "float"
                    },
                    "readposranksum": {
                        "type": "float"
                    },
                    "vqslod": {
                        "type": "float"
                    },
                    "culprit": {
                        "type": "string",
                        "analyzer": "string_lowercase"
                    }
                }
            },
            "exac_nontcga": {
                "properties": {
                    "chrom": {
                        "type": "string",
                        "analyzer": "string_lowercase"
                    },
                    "pos": {
                        "type": "long"
                    },
                    "ref": {
                        "type": "string",
                        "analyzer": "string_lowercase"
                    },
                    "alt": {
                        "type": "string",
                        "analyzer": "string_lowercase"
                    },
                    "alleles": {
                        "type": "string",
                        "analyzer": "string_lowercase"
                    },
                    "type": {
                        "type": "string",
                        "analyzer": "string_lowercase"
                    },
                    "qual": {
                        "type": "float"
                    },
                    "filter": {
                        "type": "string",
                        "analyzer": "string_lowercase"
                    },
                    "ac": {
                        "properties": {
                            "ac": {
                                "type": "integer"
                            },
                            "ac_afr": {
                                "type": "integer"
                            },
                            "ac_amr": {
                                "type": "integer"
                            },
                            "ac_adj": {
                                "type": "integer"
                            },
                            "ac_eas": {
                                "type": "integer"
                            },
                            "ac_fin": {
                                "type": "integer"
                            },
                            "ac_nfe": {
                                "type": "integer"
                            },
                            "ac_oth": {
                                "type": "integer"
                            },
                            "ac_sas": {
                                "type": "integer"
                            },
                            "ac_male": {
                                "type": "integer"
                            },
                            "ac_female": {
                                "type": "integer"
                            }
                        }
                    },
                    "af": {
                        "type": "float"
                    },
                    "an": {
                        "properties": {
                            "an": {
                                "type": "integer"
                            },
                            "an_afr": {
                                "type": "integer"
                            },
                            "an_amr": {
                                "type": "integer"
                            },
                            "an_adj": {
                                "type": "integer"
                            },
                            "an_eas": {
                                "type": "integer"
                            },
                            "an_fin": {
                                "type": "integer"
                            },
                            "an_nfe": {
                                "type": "integer"
                            },
                            "an_oth": {
                                "type": "integer"
                            },
                            "an_sas": {
                                "type": "integer"
                            },
                            "an_female": {
                                "type": "integer"
                            },
                            "an_male": {
                                "type": "integer"
                            }
                        }
                    },
                    "baseqranksum": {
                        "type": "float"
                    },
                    "clippingranksum": {
                        "type": "float"
                    },
                    "fs": {
                        "type": "float"
                    },
                    "dp": {
                        "type": "long"
                    },
                    "het": {
                        "properties": {
                            "het_afr": {
                                "type": "integer"
                            },
                            "het_amr": {
                                "type": "integer"
                            },
                            "het_eas": {
                                "type": "integer"
                            },
                            "het_fin": {
                                "type": "integer"
                            },
                            "het_nfe": {
                                "type": "integer"
                            },
                            "het_oth": {
                                "type": "integer"
                            },
                            "het_sas": {
                                "type": "integer"
                            },
                            "ac_het": {
                                "type": "integer"
                            }
                        }
                    },
                    "hom": {
                        "properties": {
                            "hom_afr": {
                                "type": "integer"
                            },
                            "hom_amr": {
                                "type": "integer"
                            },
                            "hom_eas": {
                                "type": "integer"
                            },
                            "hom_fin": {
                                "type": "integer"
                            },
                            "hom_nfe": {
                                "type": "integer"
                            },
                            "hom_oth": {
                                "type": "integer"
                            },
                            "hom_sas": {
                                "type": "integer"
                            },
                            "ac_hom": {
                                "type": "integer"
                            }
                        }
                    },
                    "inbreedingcoeff": {
                        "type": "float"
                    },
                    "mq": {
                        "properties": {
                            "mq": {
                                "type": "float"
                            },
                            "mq0": {
                                "type": "integer"
                            },
                            "mqranksum": {
                                "type": "float"
                            }
                        }
                    },
                    "ncc": {
                        "type": "long"
                    },
                    "qd": {
                        "type": "float"
                    },
                    "readposranksum": {
                        "type": "float"
                    },
                    "vqslod": {
                        "type": "float"
                    },
                    "culprit": {
                        "type": "string",
                        "analyzer": "string_lowercase"
                    }
                }
            }
        }
        return mapping


class ExacUploader(ExacBaseUploader):

    name = "exac"
    main_source= "exac"

    def load_data(self,data_folder):
        content = glob.glob(os.path.join(data_folder,"ExAC.r*.vcf"))
        if len(content) != 1:
            raise uploader.ResourceException("Expecting one single vcf file, got: %s" % repr(content))
        input_file = content.pop()
        self.logger.info("Load data from file '%s'" % input_file)
        return load_data(input_file)


class ExacNonTCGAUploader(ExacBaseUploader):

    name = "exac_nontcga"
    main_source= "exac"

    def load_data(self,data_folder):
        content = glob.glob(os.path.join(data_folder,"ExAC_nonTCGA.r*.vcf"))
        if len(content) != 1:
            raise uploader.ResourceException("Expecting one single vcf file, got: %s" % repr(content))
        input_file = content.pop()
        self.logger.info("Load data from file '%s'" % input_file)
        return load_data(input_file)
