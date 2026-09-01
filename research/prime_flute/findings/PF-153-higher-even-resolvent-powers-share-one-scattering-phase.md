# PF-153 — higher even resolvent powers do not create independent scattering phases

**Status:** `LITERATURE+DERIVED + EXACT-CONDITIONAL + NEGATIVE/BOUNDARY`. PF-146 leaves open the global trace-class gate

\[
(P_1+1)^{-2}-(P_0+1)^{-2}\in\mathcal S_1
\]

for the exact prime flute and its exact all-composite shift clone, while PF-148 shows that this single gate already recovers an ordinary Krein spectral-shift function and Birman--Krein scattering phase for the original Laplacians by the invariance principle. The present finding closes a natural but artificial extension of that program: once the squared-resolvent gate holds, replacing the square by the fourth, sixth, or any higher **even** resolvent power does not create a hierarchy of new first-order scattering phases. Every such trace-class transform pulls back to the same normalized spectral-shift function and the same physical scattering determinant. The associated trace differences are only different weighted moments of that one spectral-shift function. Thus the resolvent exponent itself cannot supply an additional zeta-like selector.

## Claim

Let `P_0,P_1 >= 0` be the two self-adjoint Laplacians after one fixed admissible common-Hilbert-space identification and put

\[
B_i=(P_i+1)^{-2},\qquad i=0,1.
\tag{1}
\]

Assume the still-open global PF-146 hypothesis

\[
\boxed{B_1-B_0\in\mathcal S_1.}
\tag{2}
\]

For every integer `k>=1`, define

\[
B_i^{(k)}:=B_i^k=(P_i+1)^{-2k},
\qquad
\phi_k(\lambda):=(1+\lambda)^{-2k}.
\tag{3}
\]

Then:

1. every higher even resolvent-power pair is again trace-class comparable,
   \[
   \boxed{B_1^{(k)}-B_0^{(k)}\in\mathcal S_1,}
   \tag{4}
   \]
   with the quantitative bound
   \[
   \boxed{
   \|B_1^{(k)}-B_0^{(k)}\|_{\mathcal S_1}
   \le k\,\|B_1-B_0\|_{\mathcal S_1},
   }
   \tag{5}
   \]
   because `0<=B_i<=I`;

2. let `xi_k` be the ordinary Krein spectral-shift function of the bounded trace-class pair `(B_1^{(k)},B_0^{(k)})`, with the standard normalization compatible with the invariance principle. Then the pulled-back spectral-shift function
   \[
   \boxed{
   \xi_P(\lambda)
   :=-\xi_k(\phi_k(\lambda))
   }
   \tag{6}
   \]
   is independent of `k` up to the usual null-set/normalization convention;

3. likewise, if `S_k` denotes the scattering matrix for the bounded pair `(B_1^{(k)},B_0^{(k)})` and `S_P` the scattering matrix for `(P_1,P_0)`, then for almost every physical energy at which the fibers are defined,
   \[
   \boxed{
   S_k(\phi_k(\lambda))\simeq S_P(\lambda)^*,
   }
   \tag{7}
   \]
   where the adjoint is the orientation reversal from the decreasing transform `phi_k`. Consequently the on-shell determinant phase obtained from any `k` is the same physical Birman--Krein phase after this fixed orientation correction;

4. the scalar trace hierarchy contains no additional first-order spectral information. For every `k>=1`, the Lifshits--Krein trace formula gives
   \[
   \boxed{
   \operatorname{Tr}\!\left((P_1+1)^{-2k}-(P_0+1)^{-2k}\right)
   =\int_0^\infty \phi_k'(\lambda)\,\xi_P(\lambda)\,d\lambda,
   }
   \tag{8}
   \]
   whenever the normalized resolvent-comparable spectral-shift convention from PF-148 is used. Thus changing `k` changes only the weight
   \[
   \phi_k'(\lambda)=-2k(1+\lambda)^{-2k-1}
   \tag{9}
   \]
   applied to the same `xi_P`.

The conclusion is deliberately about the **first-order Krein/Birman--Krein structure**. It does not identify the off-spectrum Fredholm determinants for different `k` as analytic functions, and it does not collapse PF-147's distinct `det_2`/Koplienko object for the first-resolvent Hilbert--Schmidt pair.

## 1. Trace class propagates to every even resolvent power

For bounded operators `A,C`, the noncommutative telescoping identity is

\[
A^k-C^k
=\sum_{j=0}^{k-1}
A^{k-1-j}(A-C)C^j.
\tag{10}
\]

Apply (10) with `A=B_1` and `C=B_0`. Under (2), every summand is trace class. Since `0<=B_i<=I`,

\[
\|B_1^{k-1-j}(B_1-B_0)B_0^j\|_1
\le\|B_1-B_0\|_1.
\tag{11}
\]

Summing the `k` terms proves (4)--(5). No geometry and no additional prime-gap estimate enters here. In particular, a future proof of the single global square-resolvent gate automatically supplies the entire even-power trace-class ladder.

This propagation should not be confused with a statement about **odd** powers of the first resolvent. PF-147 gives only

\[
(P_1+1)^{-1}-(P_0+1)^{-1}\in\mathcal S_2
\tag{12}
\]

under (2), and PF-112 excludes `S_1`. PF-153 therefore makes no automatic trace-class claim for arbitrary odd powers by this elementary argument.

## 2. The invariance principle identifies all pulled-back spectral shifts

Each `phi_k` is smooth and strictly decreasing on `[0,infinity)`. Equation (4) therefore places every pair

\[
\bigl(\phi_k(P_1),\phi_k(P_0)\bigr)
\tag{13}
\]

inside ordinary trace-class spectral-shift theory. Pushnitski's invariance-principle framework treats precisely the situation in which different monotone functions of the same self-adjoint pair are trace-class comparable. In his Section 7, the scattering/spectral-flow invariant is unchanged when one admissible monotone transform is replaced by another; the corresponding Krein spectral-shift functions pull back to the same normalized spectral-shift function of the original pair.

Because every `phi_k` is decreasing, the orientation sign is the same for all `k`. Thus for any `k,l>=1`,

\[
-\xi_k(\phi_k(\lambda))
=-\xi_l(\phi_l(\lambda))
\quad\text{for a.e. }\lambda,
\tag{14}
\]

which proves (6). PF-148 is the `k=1` instance of exactly this construction.

The normalization qualification matters. Spectral-shift functions can be represented only up to the standard equivalence appropriate to the chosen resolvent-comparable setup unless one fixes a normalization. PF-153 compares the transforms **within one common invariance-principle normalization**; it does not claim that arbitrary independently shifted representatives are numerically identical.

## 3. The same collapse occurs for the scattering determinant

Kato--Rosenblum applies to every trace-class bounded pair `(B_1^{(k)},B_0^{(k)})`. The Birman--Kato invariance principle then transports its wave operators back to `(P_1,P_0)`. Since `phi_k` is decreasing, the incoming/outgoing labels interchange, exactly as in PF-148, giving (7).

The ordinary Birman--Krein identity on the transformed pair is

\[
\det S_k(\mu)
=\exp\!\left(-2\pi i\,\xi_k(\mu)\right).
\tag{15}
\]

At `mu=phi_k(lambda)`, equations (6)--(7) show that every `k` yields the same physical on-shell phase after the same adjoint/orientation correction. Hence the formal family

\[
(P+1)^{-2},\ (P+1)^{-4},\ (P+1)^{-6},\ldots
\tag{16}
\]

does **not** generate independent scattering phases. It is one scattering invariant viewed through different monotone energy coordinates.

This is the decisive negative content. Without the invariance principle, the existence of infinitely many trace-class bounded transforms can look like an operator hierarchy from which one might try to manufacture a product, determinant tower, or zeta analogue. At the level of the canonical first-order scattering phase, that hierarchy is redundant.

## 4. Resolvent-power traces are moments of the same spectral-shift function

For the resolvent-comparable spectral-shift function `xi_P` obtained in PF-148, the Lifshits--Krein trace formula for an admissible test function `f` reads

\[
\operatorname{Tr}(f(P_1)-f(P_0))
=\int f'(\lambda)\xi_P(\lambda)d\lambda.
\tag{17}
\]

Taking `f=phi_k` gives (8)--(9). Therefore even the numerical relative traces

\[
T_k:=\operatorname{Tr}\!\left((P_1+1)^{-2k}-(P_0+1)^{-2k}\right)
\tag{18}
\]

should be interpreted as weighted moments of a single relative spectral object, not as new independent invariants attached to each resolvent exponent.

The sequence `{T_k}` can of course encode information about `xi_P`; a sufficiently rich moment family may help reconstruct a measure or function under additional hypotheses. PF-153 does **not** say that the traces are numerically redundant in such an inverse-problem sense. It says that their information source is already the same `xi_P`, so assigning a separate arithmetic meaning to the index `k` would import structure not supplied by the prime flute.

## 5. What is not ruled out

Several potentially meaningful objects survive this negative result.

First, the actual energy dependence of

\[
\xi_P(\lambda)
\quad\text{or}\quad
\det S_P(\lambda)
\tag{19}
\]

could still contain nonlocal information about the exact prime/shift geometry. PF-153 says only that changing the monotone resolvent transform does not multiply that information.

Second, PF-147's direct first-resolvent pair remains in the Hilbert--Schmidt/Koplienko regime under the global square-resolvent hypothesis. Its `det_2` is a genuinely different **second-order** perturbation object. Gesztesy--Pushnitski--Simon nevertheless show that Hilbert--Schmidt membership alone does not guarantee the boundary values needed for an ordinary scattering phase, so it cannot be identified with the first-order phase ladder above without extra input.

Third, the off-spectrum perturbation determinants

\[
D_k(z)
=\det\!\left((B_1^{(k)}-z)(B_0^{(k)}-z)^{-1}\right)
\tag{20}
\]

are not asserted to be literal reparametrizations of one analytic function. Their normalizations and off-spectrum analytic behavior can differ. PF-153 rules out only treating their **physical first-order spectral-shift/scattering phases** as independent selectors merely because the exponent differs.

Finally, the entire statement remains conditional on (2). PF-146 proves only fixed-central-collar trace class for the squared relative resolvent, not the global uncut hypothesis.

## 6. Prior-art / novelty audit

No novelty is claimed for any abstract operator-theoretic step in PF-153.

- **A. Pushnitski**, *The spectral shift function and the invariance principle*, Journal of Functional Analysis 183 (2001), 269--320; arXiv:`math/9911182`, DOI `10.1006/jfan.2001.3751`, develops the invariance principle for the spectral shift/scattering invariant under admissible monotone transforms. Section 7 explicitly compares two functions `f_1,f_2` of the same self-adjoint pair and proves invariance of the relevant spectral-flow/scattering data.
- **T. Kato**, *Wave operators and unitary equivalence*, Pacific Journal of Mathematics 15 (1965), 171--180, DOI `10.2140/pjm.1965.15.171`, supplies the classical wave-operator invariance background already used in PF-146/PF-148.
- Ordinary Lifshits--Krein and Birman--Krein theory supplies (15) and (17) once the bounded transformed pair is trace-class comparable.

Directed searches around higher resolvent powers, resolvent-comparable pairs, perturbation determinants, Koplienko spectral shift, and the invariance principle found this transform-independence as classical operator theory rather than a new hyperbolic-surface theorem. The project-specific contribution is only the negative specialization:

\[
\boxed{
\text{if the prime/shift square-resolvent }\mathcal S_1\text{ gate holds,}
\text{ then all even resolvent powers reuse one first-order scattering phase.}
}
\tag{21}
\]

This closes the tempting but non-intrinsic move of treating the resolvent exponent as an additional arithmetic degree of freedom.

## 7. Stress tests and falsification core

A later adversary can check PF-153 through a short finite chain:

1. verify the global hypothesis is exactly (2), not PF-146's local collar estimate;
2. check the noncommutative telescoping identity (10) and the contraction bound `||B_i||<=1`, giving (4)--(5);
3. verify that every `phi_k` is strictly decreasing and admissible for the same Pushnitski/Kato invariance-principle framework;
4. fix one common normalization and derive (14), paying attention to the minus sign from decreasing orientation;
5. apply the scattering invariance principle and Birman--Krein to obtain (7) and (15);
6. apply the Lifshits--Krein trace formula with `f=phi_k` to obtain (8);
7. do **not** infer equality of the off-spectrum determinants (20), trace class of arbitrary odd resolvent powers, analytic continuation, resonance equality, a Selberg/Ruelle product, or any RH statement.

A genuine refutation would have to show that the resolvent-power transforms fail the hypotheses of the standard invariance principle under (2), that the common normalization in (14) is inconsistent, or that the trace formula (8) does not apply to this resolvent-comparable setup. Merely observing that `D_k(z)` differs off spectrum would not refute the stated claim.

## Consequence for the research line

PF-146/PF-148 make the still-open global square-resolvent trace-class gate valuable because it would produce complete wave operators and one canonical relative Krein/Birman--Krein phase. PF-153 shows that **raising the resolvent power cannot turn that single phase into a new hierarchy of arithmetic observables**. If the global gate is eventually proved, the meaningful next question is the actual content of `xi_P(lambda)` or `det S_P(lambda)` and whether any part of it survives the all-composite control in a prime-specific way. Varying the exponent `2k` is not such a mechanism.