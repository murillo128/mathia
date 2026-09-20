# Robin-extremal research lines

This file records current mathematical questions for the Robin-extremal line. It is a mutable synthesis, not a task queue or history.

## Seek coefficient-phase interference outside same-ray serial single-center prediction

**Linked intuitions:** `MI-060-complex-single-center-drift-cannot-escape-a-fixed-prediction-corridor` and `MI-061-co-phased-serial-multicenter-has-no-wiener-discount`.

RE-229--RE-236 close the ordinary single-center escape routes far beyond the fixed-real regime. The local phase threshold, finite-ray prediction corridor and Wiener cost persist under complex drift; RE-236 removes the inverse-center proof artifact and shows that every contracting super-broad single-center family with bounded normalized Wiener rate forces an exponentially thin destination.

RE-237 tests the simplest proposed change of architecture: multiply several normalized single-center predictors. If all centers lie on one common complex ray, every factor has the same relative coefficient phase character. Convolution paths reaching a common output degree are therefore co-phased, so there is **no coefficient cancellation at all**:

`||prod_r F_r||_A = prod_r ||F_r||_A`.

The minimum delays add, and the normalized Wiener rate of the cascade is exactly the delay-weighted average of the constituent rates. A serial cascade of individually successful positive-real or same-ray predictors can never beat its best constituent merely by adding centers. In the delay-measure representation the same statement is exact multiplicativity of total variation under convolution.

The common-ray hypothesis is load-bearing. Different center phases can make convolution paths interfere, and RE-237 gives a finite algebraic example with strict Wiener submultiplicativity. Its rate conclusion also assumes the stages are individually successful predictors; a deliberately coupled product whose factors are not predictors is not covered.

The live multi-center frontier is therefore much more specific than “try several centers.” A useful architecture must make several centers contribute to the **same final coefficient with genuinely different phases before absolute values are taken**, or use parallel/additive/minimax synthesis, or arrange a coupled product whose predictive behavior exists only after composition. Those mechanisms must still beat the destination-width/Wiener-cost ledger left by the single-center results.

## Keep local flattening, destination width, coefficient phase and global Wiener cost distinct

The single-center results show that local flattening can be real while global cost destroys the gain. RE-237 adds a second representation trap: changing from one center to several centers does not change the cost mechanism if all coefficient paths remain locked to one phase character. Architectural multiplicity is not useful unless it creates an interference channel unavailable to the one-center representation.

Future candidates should therefore expose their final coefficient geometry before asymptotic optimization. If convolution paths are co-phased, Wiener cost multiplies exactly and serial composition cannot improve the normalized exponent. If phases differ, quantify the cancellation that survives DC normalization and the prediction constraint rather than relying on generic submultiplicativity. The remaining multi-center branch is an interference problem, not a center-count problem.