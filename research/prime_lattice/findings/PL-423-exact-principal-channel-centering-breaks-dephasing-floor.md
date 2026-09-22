# PL-423 — Exact principal-channel centering is incompatible with the local dephasing image cone

**Evidence/status:** `EXACT-DERIVED + PRIOR-ART-AUDITED + DECISIVE-NEGATIVE`.

**Parent findings:** `PL-421`, `PL-422`.

## Claim

`PL-422` leaves centered/model-subtracted residue covariances as a possible repair after the raw short-AP Gram collapses toward the common rank-one mode. There are, however, two mathematically different repairs hidden in that phrase. **Exact common-mode centering across residue classes is impossible inside the positive local-factor image cone of `PL-421`.** Deterministic subtraction of the expected main term is not ruled out.

Fix an odd prime `p`, put

\[
m=p-1,
\qquad
\delta_p=\frac1{p-1}=\frac1m,
\]

and let `x_a` be Hilbert-space vectors indexed by the reduced residues `a in U_p`. Define their exact residue-average and centered vectors by

\[
\bar x:=\frac1m\sum_{a\in U_p}x_a,
\qquad
q_a:=x_a-\bar x.
\tag{1}
\]

Let

\[
S^\circ=(\langle q_a,q_b\rangle)_{a,b\in U_p},
\qquad
D^\circ:=\operatorname{Diag}(S^\circ).
\tag{2}
\]

Then

\[
\sum_{a\in U_p}q_a=0,
\qquad
S^\circ\mathbf1=0.
\tag{3}
\]

If the centered family is nonzero, then `tr(D^circ)>0`. Therefore

\[
\boxed{
\mathbf1^*\left(S^\circ-\delta_pD^\circ\right)\mathbf1
=-\delta_p\operatorname{tr}(D^\circ)<0.
}
\tag{4}
\]

But `PL-421` proves that a target covariance `S` lies in the positive image of the normalized Hardy--Littlewood local-factor insertion

\[
\Psi_p(R)
=\frac{p-2}{p-1}R
+\frac1{p-1}\operatorname{Diag}(R),
\qquad R\ge0,
\tag{5}
\]

if and only if

\[
S-\delta_p\operatorname{Diag}(S)\ge0.
\tag{6}
\]

Equations (4)--(6) give the exact obstruction

\[
\boxed{
S^\circ\notin\Psi_p(M_m^+)
\quad\text{for every nonzero exactly common-mode-centered residue Gram.}
}
\tag{7}
\]

For the live `p=5` channel, exact centering creates a zero mode while positive local insertion requires normalized spectral floor `1/4`. The failure is therefore maximal: the smallest normalized eigenvalue is exactly `0`, not merely asymptotically below the required floor.

This kills **exact deletion of the principal residue-character channel** as a way to repair `PL-422` while retaining the `PL-421` positive local-factor representation. It does not kill subtraction of a deterministic Hardy--Littlewood/PNT main term, because that operation does not force the principal channel to vanish.

## 1. Centering is an exact projection onto the nonprincipal residue subspace

Write the residue family as a column vector `x=(x_a)_{a in U_p}` and let

\[
H_m:=I-\frac1m\mathbf1\mathbf1^*.
\tag{8}
\]

Then exact common-mode centering is simply

\[
q=H_mx,
\qquad
S^\circ=H_mSH_m,
\tag{9}
\]

where `S=(<x_a,x_b>)`. Since

\[
H_m\mathbf1=0,
\tag{10}
\]

we obtain (3) and

\[
\operatorname{rank}(S^\circ)\le m-1.
\tag{11}
\]

In the finite Fourier basis of multiplicative characters of `U_p`, the vector `m^{-1/2}1` is the principal-character direction. Thus `H_m` removes that channel exactly and leaves the orthogonal sum of the nonprincipal character channels. The zero eigenvalue in (11) is not a statistical approximation; it is the algebraic signature of exact principal-channel deletion.

This observation is standard finite-dimensional centering/character orthogonality. The line-specific content begins when it is compared with the positive local-factor image cone from `PL-421`.

## 2. Positive local insertion forbids such a zero mode

`PL-421` identifies the image cone exactly. If

\[
S=\Psi_p(R),
\qquad R\ge0,
\tag{12}
\]

then

\[
S-\delta_p\operatorname{Diag}(S)
=\frac{p-2}{p-1}R
\ge0.
\tag{13}
\]

For `S=S^circ`, test (13) on the principal vector `1`. By (3),

\[
\mathbf1^*S^\circ\mathbf1
=\left\|\sum_a q_a\right\|^2
=0,
\tag{14}
\]

whereas

\[
\mathbf1^*D^\circ\mathbf1
=\sum_a\|q_a\|^2
=\operatorname{tr}(D^\circ)>0
\tag{15}
\]

for every nontrivial centered family. Hence (4), contradicting (13).

There is an equivalent spectral formulation when the diagonal is positive. Let

\[
C^\circ=(D^\circ)^{-1/2}S^\circ(D^\circ)^{-1/2}.
\tag{16}
\]

From `S^circ 1=0`,

\[
C^\circ(D^\circ)^{1/2}\mathbf1=0,
\tag{17}
\]

so

\[
\lambda_{\min}(C^\circ)=0.
\tag{18}
\]

The exact image criterion of `PL-421` instead requires

\[
\lambda_{\min}(C^\circ)\ge\frac1{p-1}>0.
\tag{19}
\]

Thus exact centering and positive local insertion are structurally incompatible for every odd prime, independently of any asymptotic prime-distribution estimate.

A slightly more general statement follows for free. On its positive-diagonal support, every nonzero matrix in `Psi_p(M_m^+)` is positive definite because the `delta_p Diag(R)` term supplies a strictly positive private component in every active coordinate. Consequently **any exact linear dependence among active residue vectors excludes membership in the local dephasing image cone**. Common-mode centering is simply the canonical arithmetic instance, with dependence vector `1`.

## 3. Why deterministic model subtraction is different

For the short-interval vectors of `PL-422`,

\[
P_a(y;h)
=
\sum_{\substack{y<n\le y+h\\n\equiv a\pmod p}}\Lambda(n),
\tag{20}
\]

there are at least two natural ways to remove the common leading mode.

Exact data-dependent centering uses

\[
q_a(y;h)
=P_a(y;h)-\frac1m\sum_{b\in U_p}P_b(y;h).
\tag{21}
\]

It satisfies `sum_a q_a=0` identically for every `y`, hence is ruled out by (7).

Deterministic model subtraction instead uses

\[
r_a(y;h)
=P_a(y;h)-\frac hm.
\tag{22}
\]

Now

\[
\sum_{a\in U_p}r_a(y;h)
=
\sum_{a\in U_p}P_a(y;h)-h,
\tag{23}
\]

which is the total short-interval prime-counting fluctuation (up to the finitely many integers divisible by `p`, depending on the precise convention). It is not identically zero. Therefore the principal-character component survives as a genuine fluctuation channel, and the Gram of the `r_a` need not be singular.

In character coordinates, with the unitary normalization on `U_p`, the principal coefficient is

\[
A_{\chi_0}(y)
=\frac1{\sqrt m}
\left(\sum_aP_a(y;h)-h\right),
\tag{24}
\]

whereas for nonprincipal `chi`,

\[
A_\chi(y)
=\frac1{\sqrt m}
\sum_a\overline{\chi(a)}P_a(y;h).
\tag{25}
\]

Exact centering sets (24) to zero by construction. Model subtraction leaves (24) available to supply the missing direction required by the lower-Riesz-floor condition.

This distinction matters because the negative result in `PL-422` came from a deterministic common main term dominating the raw covariance. Removing that deterministic mode is still a live repair. What is now closed is the stronger operation of projecting the data itself onto the nonprincipal-character subspace.

## 4. Prior-art and novelty audit

The individual ingredients are standard. Centering by `H_m=I-m^{-1}11*` and the resulting rank deficiency are elementary covariance/Gram linear algebra. Character orthogonality identifies the constant residue vector with the principal Dirichlet character. The general language of Schur/dephasing maps and covariance shrinkage was already audited in `PL-421`.

Targeted literature searches across dephasing/Schur multipliers, centered covariance matrices, short-interval primes in arithmetic progressions, and Dirichlet-character covariance did not locate a source combining these ingredients into the exact obstruction (4)--(7) for the Hardy--Littlewood local-factor image cone. No novelty is claimed for centering, singular covariance matrices, character Fourier transforms, or dephasing channels themselves.

The durable line-specific statement is narrower: **the exact principal-character projection suggested as a repair after `PL-422` is disjoint from the positive image of the arithmetic dephasing map characterized in `PL-421`, except at the zero matrix**. The proof is finite-dimensional and exact.

## 5. Adversarial audit

1. **This does not rule out deterministic centering.** Subtracting `h/(p-1)` from every residue vector removes the asymptotic main term but does not impose an exact linear relation. Equation (23) is precisely the surviving channel that must be analyzed next.

2. **This does not rule out a different positive representation.** The obstruction applies to the specific local-factor map `Psi_p` derived in `PL-421`. A nonlocal lift, a larger dilation, an indefinite/Krein-space representation, or a zero-side construction could evade it, but would need independent mathematical justification.

3. **Zero diagonal entries do not create an escape.** The direct witness (4) does not require inverting `D^circ`. If the centered family is nonzero, `tr(D^circ)>0` and the inverse-cone test fails. If every centered vector is zero, the Gram is the trivial zero matrix.

4. **No prime-distribution theorem is being smuggled in.** The obstruction holds for arbitrary Hilbert-space vectors indexed by `U_p`; no PNT, GRH, pair-correlation estimate, or analytic continuation is used.

5. **The result is a pruning theorem, not an RH criterion.** It says that one natural way of repairing the raw covariance cannot coexist with exact positive local-factor deletion. It neither proves nor disproves the lower spectral floor for the remaining model-subtracted covariance.

## Consequence for the line

The phrase “centered/model-subtracted covariance” after `PL-422` must be split into two distinct branches. The exact projection

\[
x_a\mapsto x_a-\frac1m\sum_bx_b
\tag{26}
\]

is closed: it necessarily creates the zero mode forbidden by the `1/(p-1)` image-cone floor.

The surviving canonical test is instead the deterministic residual

\[
P_a(y;h)-\frac h{p-1}.
\tag{27}
\]

For `p=5`, the next falsifiable question is whether the normalized Gram of these four model-subtracted residue fluctuations can satisfy

\[
\lambda_{\min}(C_X)\ge\frac14
\tag{28}
\]

in a non-circular range, or whether character-channel variance/cross-covariance forces another obstruction. Unlike exact centering, that question retains the principal short-interval fluctuation and therefore is not settled by linear algebra alone.
