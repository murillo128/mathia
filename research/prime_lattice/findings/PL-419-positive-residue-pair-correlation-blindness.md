# PL-419 — Positive residue-class pair-correlation aggregates miss the mod-5 supertrace contrast; off-diagonal residue coherence is mandatory

**Evidence/status:** `EXACT-DERIVED + LITERATURE-CALIBRATED + DECISIVE-REPRESENTATION-OBSTRUCTION`.

**Parent findings:** `PL-415`, `PL-416`, `PL-418`.

## Claim

`PL-415` isolates the exact away-from-5 source target as the signed character-channel quadratic form

\[
D=\operatorname{diag}(15,-1,-1,-1)
\tag{1}
\]

in the four Dirichlet-character channels modulo `5`. A natural zero-side attempt is to use the positive residue-class pair-correlation aggregates introduced in the Dirichlet-`L` literature: first retain the full cross-character zero-correlation matrix and then evaluate it in each residue-class character vector. That route preserves positivity, but **the resulting positive residue aggregates do not determine the `PL-415` supertrace, even if all four reduced residues are used simultaneously**.

In the notation of Kandhil--Languasco--Moree, fix `(x,T)` and let

\[
G=(G_{\chi,\psi}(x,T))_{\chi,\psi\bmod 5}
\tag{2}
\]

be the four-character pair-correlation matrix. Their definition uses, under GRH,

\[
G_{\chi,\psi}(x,T)
=\sum_{|\gamma_\chi|,|\gamma_\psi|\le T}
 x^{i(\gamma_\chi-\gamma_\psi)}
 W(\gamma_\chi-\gamma_\psi).
\tag{3}
\]

The Fourier representation of `W` makes `G` a Gram matrix for the corresponding zero sums, hence `G>=0`. For each reduced residue `a mod 5`, put

\[
w_a=
\begin{pmatrix}
\chi_0(a)\\
\chi_2(a)\\
\chi_4(a)\\
\overline{\chi_4}(a)
\end{pmatrix}.
\tag{4}
\]

Their positive residue aggregate is exactly

\[
\boxed{
F_5(a)=w_a^*G w_a\ge0.
}
\tag{5}
\]

The `PL-415` diagonal character contrast, applied to any such matrix-valued pair-correlation kernel, is instead

\[
\boxed{
S_D(G):=\operatorname{tr}(DG).
}
\tag{6}
\]

There is no choice of coefficients `c_a` for which

\[
S_D(G)=\sum_{a\in(\mathbb Z/5\mathbb Z)^\times}c_aF_5(a)
\tag{7}
\]

holds for all Hermitian `G`. More strongly, the entire four-vector `(F_5(1),F_5(2),F_5(3),F_5(4))` fails to determine `S_D(G)` even on the positive-semidefinite class. The missing information is exactly **off-diagonal coherence in the residue basis**.

This closes the shortcut

\[
\text{PL-415 signed character supertrace}
\longrightarrow
\text{positive residue-class pair correlations }F_5(a)
\longrightarrow
\text{power saving},
\]

unless an additional arithmetic theorem links the missing coherences to the positive residue energies. Such a theorem would be new input; it is not supplied by character orthogonality or by positivity of `F_5(a)`.

## 1. The four positive residue readouts span the wrong matrix algebra

Let

\[
P_a:=w_aw_a^*.
\tag{8}
\]

Then `F_5(a)=tr(GP_a)`. Since every Dirichlet character has modulus one on a reduced residue, every `P_a` has the same diagonal:

\[
\operatorname{diag}(P_a)=(1,1,1,1).
\tag{9}
\]

Consequently every linear combination

\[
\sum_a c_aP_a
\tag{10}
\]

has constant diagonal `(sum_a c_a)I` on the diagonal entries. The required matrix (1) has diagonal `(15,-1,-1,-1)`, so

\[
\boxed{
D\notin\operatorname{span}\{P_a:a\in(\mathbb Z/5\mathbb Z)^\times\}.
}
\tag{11}
\]

This already proves that no linear combination of the positive residue aggregates can reproduce the exact signed diagonal statistic for arbitrary `G`.

The failure is quantitatively transparent. The normalized vectors

\[
u_a:=\frac12w_a
\tag{12}
\]

form an orthonormal basis by character orthogonality. Hence the four rank-one matrices `P_a` are mutually Hilbert--Schmidt orthogonal, with

\[
\langle P_a,P_b\rangle_{HS}=16\,\delta_{ab}.
\tag{13}
\]

Moreover

\[
\langle D,P_a\rangle_{HS}
=w_a^*Dw_a
=15-1-1-1=12
\tag{14}
\]

for every `a`, and

\[
\sum_aP_a=4I.
\tag{15}
\]

Therefore the Hilbert--Schmidt projection of `D` onto the complete positive-residue span is

\[
\boxed{
\Pi_{\rm res}D=3I,
}
\tag{16}
\]

while the contrast

\[
\boxed{
D-3I=\operatorname{diag}(12,-4,-4,-4)
}
\tag{17}
\]

is orthogonal to **every** residue projector `P_a`. Thus the part of the mod-5 metric that distinguishes the principal channel from the three nonprincipal channels lies precisely in the blind complement of the positive residue readouts.

There is also an exact matched structural control on the PSD class. Take

\[
G_+=\operatorname{diag}(1,0,0,0),
\qquad
G_-=\operatorname{diag}(0,1,0,0).
\tag{18}
\]

Both are positive semidefinite. For every reduced residue `a`,

\[
F_5(a;G_+)=F_5(a;G_-)=1,
\tag{19}
\]

because all character values have modulus one. Yet

\[
\boxed{
S_D(G_+)=15,
\qquad
S_D(G_-)=-1.
}
\tag{20}
\]

So even knowing all four positive `F_5(a)` exactly does not determine the signed supertrace on the natural formal Gram class.

## 2. In the residue basis the missing datum is exactly off-diagonal coherence

Let `U` be the unitary character table whose columns are the vectors `u_a=w_a/2`, and transform the correlation matrix to residue coordinates:

\[
R:=U^*GU.
\tag{21}
\]

Equation (5) becomes

\[
\boxed{
F_5(a)=4R_{aa}.
}
\tag{22}
\]

Thus the established positive residue aggregates are exactly the **diagonal energies** of `R`.

Now transform the `PL-415` metric itself:

\[
K:=U^*DU.
\tag{23}
\]

For `a=b`, character orthogonality gives

\[
K_{aa}=\frac14(15-3)=3.
\tag{24}
\]

For `a\ne b`, the sum of the three nonprincipal characters of `b/a` is `-1`, hence

\[
K_{ab}=\frac14(15+1)=4.
\tag{25}
\]

Therefore

\[
\boxed{
K=4\mathbf 1\mathbf 1^*-I,
\qquad
K_{ab}=\begin{cases}3,&a=b,\\4,&a\ne b.\end{cases}
}
\tag{26}
\]

and, using the exact local inverse factor of `PL-415`,

\[
\boxed{
K_{ab}=\frac{15}{4}\,g_5(a/b).
}
\tag{27}
\]

The source repair therefore reappears in the residue basis not as a diagonal positive weight but as a dense coherence kernel.

Since traces are basis invariant,

\[
S_D(G)=\operatorname{tr}(KR).
\tag{28}
\]

For Hermitian `R`, equations (22) and (26) give the exact decomposition

\[
\boxed{
S_D(G)
=\frac34\sum_aF_5(a)
+8\sum_{\{a,b\},\,a<b}\Re R_{ab}.
}
\tag{29}
\]

The first term is fully visible to the positive residue aggregates. The second consists of the six off-diagonal residue coherences and is completely absent from those diagonal readouts. Equation (29) is the sharp representation-level form of the obstruction: **the exact mod-5 repair requires interference between residue sectors, not merely their positive energies**.

Full cross-residue matrix elements `u_a^*Gu_b`, `a\ne b`, would of course restore the missing information. But those quantities are no longer nonnegative scalar pair-correlation observables. This is the same positivity-versus-fidelity split already encountered in `PL-416`--`PL-418`, now inside the established Dirichlet-`L` pair-correlation architecture.

## 3. The phenomenon is the general local inverse-factor geometry, not a numerical accident at 5

The exact control extends to the odd-prime local factor already derived in `PL-415`. For an odd prime `p`, the inverse pair-density multiplier on the unit group has the character decomposition

\[
g_p(m-n)
=\chi_0(n)\overline{\chi_0(m)}
-\frac1{p(p-2)}
\sum_{\chi\ne\chi_0\bmod p}
\chi(n)\overline{\chi(m)}.
\tag{30}
\]

Scale its character metric to

\[
D_p=\operatorname{diag}(p(p-2),-1,\ldots,-1),
\tag{31}
\]

of size `p-1`, and let `U_p` be the normalized character table of `(Z/pZ)^times`. A direct character sum gives

\[
(U_p^*D_pU_p)_{ab}
=\begin{cases}
p-2,&a=b,\\
p-1,&a\ne b,
\end{cases}
\tag{32}
\]

or equivalently

\[
\boxed{
(U_p^*D_pU_p)_{ab}
=\frac{p(p-2)}{p-1}\,g_p(a/b).
}
\tag{33}
\]

Every positive residue projector still has constant diagonal in character coordinates, whereas `D_p` is non-scalar. Thus positive residue energies alone miss the local inverse-factor contrast for every odd prime. The `p=5` case is singled out here only because it is the unique local repair currently required by the live cubic source construction; no broader RH claim is inferred from (30)--(33).

## 4. Prior art and novelty audit

The pair-correlation architecture is established literature, not a Mathia construction.

- **C. Yalcin Yildirim**, “The pair correlation of zeros of Dirichlet L-functions and primes in arithmetic progressions,” *Manuscripta Mathematica* **72** (1991), 325--334, DOI `10.1007/BF02568283`, introduced the relevant residue-weighted Dirichlet-`L` pair-correlation framework.
- **Neelam Kandhil, Alessandro Languasco, Pieter Moree**, “Pair correlation of zeros of Dirichlet L-functions: a possible path towards the conjectures of Chowla, Elliott-Halberstam and Montgomery,” *Mathematische Annalen* **394** (2026), Article 43, DOI `10.1007/s00208-026-03383-y`, define the cross-character matrix entries `G_{chi_1,chi_2}` and the residue aggregate `F_q(x,T;a)`. Their equations (6)--(7) express `F_q` as the integral of an absolute square, proving `F_q>=0`; their zero-side results are stated under GRH.
- **H. M. Bui, J. P. Keating, D. J. Smith**, “On the variance of sums of arithmetic functions over primes in short intervals and pair correlation for L-functions in the Selberg class,” *Journal of the London Mathematical Society* **94**(1) (2016), 161--185, DOI `10.1112/jlms/jdw030`, provides the broader variance/pair-correlation transfer context for the degree-one character channels used by `PL-415`.

The finite Fourier facts used in (8)--(33) are elementary and no novelty is claimed for character orthogonality, rank-one projectors, circulant/Fourier conjugation, or Gram positivity. Targeted comparison with the above literature did not locate the line-specific statement that the exact inverse-`p=5` Hardy--Littlewood repair has its non-scalar character contrast orthogonal to all positive residue projectors, nor the explicit residue-basis identity (27)--(29). The durable contribution is therefore narrow: **within the exact `PL-415` source geometry, the established positive residue-class pair-correlation compression discards precisely the off-diagonal residue coherence needed by the repair**.

This is a representation obstruction, not a new zero-density, pair-correlation, or RH theorem.

## 5. Adversarial audit

The obstruction has several important scope limits.

1. Kandhil--Languasco--Moree place their zeros on `1/2+i gamma` under GRH. The present finding does **not** import GRH into the Mathia line. Their construction is used as prior art for the coefficient architecture and positivity of the residue aggregate; equations (8)--(33) are finite-dimensional algebra once a matrix `G` is given.

2. The controls `G_+` and `G_-` in (18) are formal positive-semidefinite matched controls. They are not claimed to arise from actual zero sets of Dirichlet `L`-functions. Their role is to prove that positivity plus the complete vector of residue readouts does not, by itself, recover the target functional.

3. Actual arithmetic correlation matrices may obey additional relations beyond positivity. If such a relation reconstructs the missing coherences from the diagonal residue energies, that relation would evade the control and would be exactly the new arithmetic theorem required by this route. No such relation is assumed or ruled out here.

4. The obstruction is pointwise in the pair-correlation parameters. An entire family `F_5(a;x,T)` as `(x,T)` vary can carry analytic constraints not visible in one matrix. Any proposed recovery from the whole family must exhibit and prove those constraints; it cannot follow from the residue projections alone.

5. The finding does not claim that the exact `PL-415` cubic source kernel has already been transferred to the particular `W` used by Kandhil--Languasco--Moree. It tests the natural **matrix architecture** of a zero-side pair-correlation route. Kernel matching and analytic continuation remain separate gates.

6. Retaining the full matrix `R`, or equivalently all cross-character entries of `G`, removes the information-theoretic obstruction. What is closed is only the positive-diagonal compression `G -> {F_5(a)}` as a sufficient representation of the signed supertrace.

7. No implication toward RH is claimed. Even a power-saving theorem for the full signed block statistic must still pass the source-replacement, continuation and final localization gates already separated by `PL-407`--`PL-418`.

## Consequence for the research line

The live `PL-415` target should not be attacked by proving or combining only the positive residue-class quantities `F_5(a)`. Those observables retain the diagonal residue energies but project away the principal-versus-nonprincipal contrast that the inverse local factor needs.

The surviving zero-side target is sharper: preserve enough of the **full cross-residue / cross-character matrix** to control the off-diagonal coherence term in (29), or estimate the signed character supertrace directly on the prime side. Any positivity-based compression must prove an additional arithmetic reconstruction theorem before it can replace that matrix data.

This also reinforces the separation established by `PL-418`. Positive quadratic packaging can make a spectral or pair-correlation object well behaved while erasing the exact source contrast. For the current mod-5 bridge, source fidelity lives in the coherence that positivity-by-diagonalization discards.