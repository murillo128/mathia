# MI-016 — Weil-form observability is stronger than moment observability, and a semilocal core is already complete

**Evidence level:** literature-backed positive-proportion localization, classical finite-defect inertia, and semilocal Laurent-core finite detectability through PL-261

## Core intuition

Finite-dimensionality is not the decisive information loss in Weil-form approaches. A finite Hermitian compression can already turn prime-power explicit-formula data into unconditional critical-line localization, while the same broad form information may lose sparse exceptional structure if it is compressed further to a few normalized moments. More strongly, one canonical nested finite Weil family is already complete enough that **every** RH failure eventually creates a finite negative direction.

The unresolved problem is therefore not how to make the finite observations complete. It is how to force their **sign** from source-side arithmetic without importing the RH-equivalent positivity conclusion.

## Strongest justified principle

PL-259 records the Alpöge--Furman theorem: a source-determined finite compression of Weil's Hermitian form, together with first and second arithmetic moments, forces more than two thirds of zeros in a window to be simple and on `Re(s)=1/2`, with optimized proportion about `0.6725`. Lamzouri's parallel proof shows that the durable input is the Weil/pair-correlation moment structure rather than one matrix realization. Those aggregate inputs are nevertheless insensitive to `o(N)` off-line populations.

PL-260 prevents that limitation from being attributed to finite forms themselves. Bombieri's classical theorem says that if only finitely many zeros are off line, the negative index of his finite Weil truncations eventually stabilizes at half their number. Exact sign structure retains a sparse integer defect that normalized moments can average away.

PL-261 closes the remaining existential sparse-infinite observability concern for the Connes--Consani semilocal family. Laurent polynomials are a form core for `QW_lambda`, and the lower bound of the closed form is the limit of the smallest eigenvalues on the nested spaces `E_N=span{U^k: |k|<=N}`. Since positivity of all semilocal forms implies RH, any RH failure yields some `lambda` with negative lower bound and therefore a finite `N_0` after which every `E_N` compression has a negative eigenvalue. No finiteness or density assumption on the off-line divisor is needed.

## Program consequence

Stop treating finite Galerkin completeness as the missing bridge for this semilocal route. The next theorem must constrain the sign of the finite source-forced forms themselves, preferably through arithmetic structure demonstrably cheaper than the full Weil criterion. A new finite basis, more moments, or another completeness proof is not progress unless it provides such a sign mechanism.

Mixed-prime exponent geometry must likewise earn its role by producing a sign/rigidity principle beyond the prime-power axis explicit formula; PL-261 already obtains finite detectability without using the interior exponent lattice.

## Counterevidence / boundary

The Connes--Consani result is existential in both the semilocal scale and the finite dimension and applies to its specific nested Laurent core. It does not give effective bounds for where a hypothetical RH failure becomes visible, Bombieri-style exact negative-index counting, or automatic conclusions for other truncation families.

Most importantly, detectability is not positivity. The core theorem gives no unconditional reason that the finite eigenvalues are nonnegative. Proving all required signs may remain essentially as hard as Weil positivity unless additional source structure is found.

## Epistemic status

**Supported observability hierarchy with the existential gap closed in one canonical family: bulk moments force a positive critical-line proportion but can miss sparse defects; exact finite-form inertia detects finite defects; the Connes--Consani semilocal Laurent core finitely detects every RH failure. The live burden is source-side sign coercivity, not completeness.**

## Falsification criterion

Produce an RH-failing configuration compatible with the semilocal Weil criterion for which every finite Laurent compression remains nonnegative, contrary to the form-core/lower-bound deduction, or show that the PL-261 use of the Connes--Consani core theorem does not imply eventual finite negativity at a scale with negative closed-form lower bound.
