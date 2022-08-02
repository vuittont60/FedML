from fedml.core import ServerAggregator


class FedMLCrossSiloServer:
    def __init__(self, args, device, dataset, model, server_aggregator: ServerAggregator = None):
        if args.federated_optimizer == "FedAvg":
            from fedml.cross_silo.server import server_initializer

            [
                train_data_num,
                test_data_num,
                train_data_global,
                test_data_global,
                train_data_local_num_dict,
                train_data_local_dict,
                test_data_local_dict,
                class_num,
            ] = dataset
            self.fl_trainer = server_initializer.init_server(
                args,
                device,
                args.comm,
                args.rank,
                args.worker_num,
                model,
                train_data_num,
                train_data_global,
                test_data_global,
                train_data_local_dict,
                test_data_local_dict,
                train_data_local_num_dict,
                server_aggregator,
            )

        elif args.federated_optimizer == "LSA":
            from .lightsecagg.lsa_fedml_api import FedML_LSA_Horizontal

            self.fl_trainer = FedML_LSA_Horizontal(
                args,
                0,
                args.worker_num,
                args.comm,
                device,
                dataset,
                model,
                model_trainer=model_trainer,
                preprocessed_sampling_lists=None,
            )
        else:
            raise Exception("Exception")

    def run(self):
        pass