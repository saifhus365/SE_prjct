#include "calcbmi.h"
#include <gtk/gtk.h>

double calc_weight(int weight, int factor)
{
	double act_weight = (((weight * 10) * 100) / ( 1000 - factor));
	g_print("\nact_weight: %f\n",act_weight );
	return act_weight;
}

double calc_bmi(int weight, double height, int factor)
{
	double act_bmi = calc_weight(weight, factor) / ((height/100) * (height/100));
	g_print("\nact_bmi: %f\n",act_bmi);
	return act_bmi;
}

