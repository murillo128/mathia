# PF-354 — prime cuff lengths are rationally independent and have no common nonzero frequency

**Status:** EXACT-DERIVED + CLASSICAL-GALOIS-METHOD + EXACT-FREQUENCY-OBSTRUCTION + NORMALIZED-ANGLE-OPEN.

The distinguished cuff lengths of the exact prime flute are linearly independent over `Q`: every finitely supported rational relation among them is trivial. Consequently, the physical Fourier lattices of any two distinct distinguished cuffs intersect only at zero. PF-353's complete common-frequency witness therefore cannot be installed exactly on two or more actual prime cuffs.

The obstruction is an exact arithmetic property of the intrinsic lengths. It gives no quantitative separation of nearby frequencies and does not decide the globally shorted angle. Moreover, it holds for pairwise coprime odd **composite** endpoint labels as well. It is not a primality detector.

## 1. Exact cuff lengths as logarithms of algebraic numbers

For consecutive odd primes `p<q`, write

\[
u_p=\cot(\pi/p),\qquad r_p=\sqrt{u_p}>0,
\qquad h_{pq}=\log(u_q/u_p).
\]

PF-032's exact cuff formula, also used by PF-107 and PF-352, gives

\[
L_{pq}=2\log\coth(h_{pq}/4)=2\log A_{pq},
\qquad
\boxed{A_{pq}=\frac{r_q+r_p}{r_q-r_p}>1.}
\tag{1}
\]

Here `u_p<u_q`, so the denominator is positive. The full cuff length `L` is the Fermi tangential period used in PF-205/PF-344; moving to a parallel seam does not change that coordinate period. Equation (1) concerns exact lengths, not their prime-gap asymptotics.

We prove a finite statement that includes every finite set of distinguished cuffs. Let `m_1<...<m_d` be distinct, pairwise coprime odd integers at least `3`, put `u_j=cot(pi/m_j)` and `r_j=sqrt(u_j)>0`, and define

\[
A_{ij}=\frac{r_j+r_i}{r_j-r_i}>1\qquad(i<j).
\tag{2}
\]

Then the family of **all distinct unordered pairs** in (2) is multiplicatively independent:

\[
\boxed{\prod_{i<j}A_{ij}^{n_{ij}}=1,\quad n_{ij}\in\mathbb Z
\quad\Longrightarrow\quad n_{ij}=0\text{ for every }i<j.}
\tag{3}
\]

Only consecutive pairs are interpreted as distinguished cuffs of the given flute. The other quantities in (2) are auxiliary algebraic expressions; this proof does not identify them with its multi-gap geodesic lengths.

## 2. Change one endpoint sign while fixing the others

Set

\[
N=4\prod_{j=1}^d m_j,\qquad F=\mathbb Q(\zeta_N),
\qquad \zeta_n=e^{2\pi i/n}.
\]

The exact identity

\[
u_j=i\,\frac{\zeta_{m_j}+1}{\zeta_{m_j}-1}
\tag{4}
\]

places every `u_j` in `F`. Fix a vertex `v`. The Chinese remainder theorem supplies a unit `a_v mod N` with

\[
a_v\equiv1\pmod4,\qquad
a_v\equiv-1\pmod{m_v},\qquad
a_v\equiv1\pmod{m_j}\quad(j\ne v).
\tag{5}
\]

The classical cyclotomic Galois theorem gives the automorphism
`sigma_v(zeta_N)=zeta_N^(a_v)`. It fixes `i`, inverts only `zeta_(m_v)` among the displayed roots, and therefore

\[
\boxed{\sigma_v(u_v)=-u_v,\qquad
\sigma_v(u_j)=u_j\quad(j\ne v).}
\tag{6}
\]

Extend this embedding to
`E=F(r_1,...,r_d)` with values in `C`, using the ordinary extension theorem for algebraic embeddings. No claim that the radicals are independent is required. Any such extension satisfies

\[
\widetilde\sigma_v(r_v)\in\{ir_v,-ir_v\},\qquad
\widetilde\sigma_v(r_j)\in\{r_j,-r_j\}\quad(j\ne v).
\tag{7}
\]

The signs in (7) need not be freely selectable; the following argument works for every possible choice.

If an edge `{i,j}` contains `v`, its transformed numerator and denominator have equal absolute value, since one root is real and the other purely imaginary. If it does not contain `v`, the transformed quotient is either `A_ij` or its reciprocal. Thus

\[
\boxed{
|\widetilde\sigma_v(A_{ij})|=
\begin{cases}
1,&v\in\{i,j\},\\
A_{ij}^{\epsilon_{ij}},\quad\epsilon_{ij}\in\{-1,1\},
&v\notin\{i,j\}.
\end{cases}}
\tag{8}
\]

All denominators remain nonzero. The unaffected roots have unequal positive magnitudes; an affected pair has one nonzero real and one nonzero imaginary root. Absolute value is taken **after** applying the algebraic embedding. No order-preserving embedding or Galois action on a chosen logarithm is being assumed.

## 3. A relation of minimal support cannot survive

Suppose (3) fails, and choose an integer relation with the smallest nonempty support `S` of edges. Since every `A_ij>1`, one edge alone cannot support a relation.

For any set `S` of at least two distinct edges, there is a vertex incident to some but not all of them: choose two different edges and a vertex in one but not the other. Apply its embedding to the multiplicative relation and then take absolute values. Equation (8) gives

\[
\prod_{\{i,j\}\in S:\ v\notin\{i,j\}}
A_{ij}^{\epsilon_{ij}n_{ij}}=1.
\tag{9}
\]

The surviving support is nonempty and strictly smaller than `S`, and every surviving exponent is still a nonzero integer. This contradicts minimality and proves (3).

Now clear denominators in any finite rational relation among the prime-cuff lengths in (1) and exponentiate half the relation. Its endpoint primes are pairwise coprime, and its distinct adjacent pairs are a subset of (2), so (3) forces all coefficients to vanish. In particular,

\[
\boxed{L_n/L_m\notin\mathbb Q\qquad(n\ne m).}
\tag{10}
\]

This establishes rational linear independence, not algebraic independence of the lengths or of their reciprocals.

## 4. Consequence for the actual Fourier lattices

Let

\[
\mathcal F_n=\{2\pi k/L_n:k\in\mathbb Z\}.
\]

A common nonzero frequency would give `k/L_n=l/L_m` with nonzero integers `k,l`, hence `L_n/L_m=k/l`, contradicting (10). Therefore

\[
\boxed{\mathcal F_n\cap\mathcal F_m=\{0\}\qquad(n\ne m).}
\tag{11}
\]

The same conclusion holds for common nonzero absolute frequencies, relevant to the cosine kernel `x=cosh(pi xi)`. Reversing cuff orientation or choosing the zero-twist foot as origin does not change the frequency set.

PF-353 requires two distinct frequencies present on **every** module in its positive network matrix. A section containing at least two different prime cuffs has only the constant frequency in common. Thus its exact complete-fibre identity does not supply a prime-flute low/high witness. PF-352's control has the exact common frequency `2` because its periods have rational ratio `(2N-1)/(2N)`; that feature is forbidden for prime cuffs. Its model cancellation and PF-353's model angle theorem remain valid.

This is an obstruction to that exact transplant, not to an approximate or differently organized witness. For any period `L_n` and target frequency `xi`, a nearest Fourier index satisfies

\[
\left|\frac{2\pi k_n}{L_n}-\xi\right|\le\frac\pi{L_n}.
\tag{12}
\]

Hence exact nonintersection supplies no positive uniform frequency gap as the periods grow. Transferring PF-353 through near-common modes still requires estimates relative to the **same shorted diagonal energies**, plus the pant/seam and finite-section controls already missing there. Neither compactness nor noncompactness of the completed angle follows from (11).

## 5. Controls, prior art and verification boundary

The proof uses pairwise coprimality and oddness, not primality: the ordered labels `m_j=p_j^2` for distinct odd primes give an all-composite endpoint control with the same rational independence. It does not establish the statement for arbitrary composite sets with shared factors, for even labels, or for the `p=2` degenerate endpoint. Multiplicative rescaling of every endpoint leaves (1) unchanged, so this is a property of the cuff lengths, not an absolute endpoint-position gauge.

The algebraic ingredients are classical. J. S. Milne, [*Fields and Galois Theory*](https://www.jmilne.org/math/Books/FT0.pdf), Proposition 2.4 and Lemma 5.9/Theorem 5.10, supplies extension of algebraic embeddings and the full cyclotomic Galois action. The CRT sign choice, the modulus calculation and the minimal-support proof are written out above. No theorem about transcendence of logarithms is imported.

The relationship between rational geodesic-length ratios and multiplicative relations of algebraic eigenvalues is established prior-art territory; compare G. Prasad and A. S. Rapinchuk, [*Weakly commensurable arithmetic groups, lengths of closed geodesics and isospectral locally symmetric spaces*](https://arxiv.org/abs/0705.2891), introduction and Section 8. Their arithmetic-group conclusions are not applied to this infinite-type flute. The cuff transform itself is the standard collar identity already audited in PF-032, with the tight-flute context in Basmajian--Hakobyan--Šarić, [*The type problem for Riemann surfaces via Fenchel–Nielsen parameters*](https://arxiv.org/abs/2011.03166).

The derived addition is the explicit endpoint-sign argument for these exact sampled cuff lengths and its exclusion of PF-353's common-frequency hypothesis on the actual prime flute. Searches by cotangent multiplicative independence, rational independence of hyperbolic lengths, and cyclotomic conjugation did not identify this exact specialization; that does not establish historical novelty. The classification is an exact specialization using classical methods.

Supplementary Python standard-library checks reduced the cross-multiplied identities (4)--(6) exactly modulo cyclotomic polynomials: labels `(3,5,7)` used conductor `420` and sign-flip exponents `(281,169,181)`, while composite labels `(9,25)` used conductor `900` and exponents `(701,649)`. All 13 endpoint-image checks passed. An exhaustive check of the 1,013 edge subsets with at least two edges on five vertices verified the support-reduction combinatorial condition. These checks are consistency tests; the arbitrary finite theorem follows from (4)--(9), not from a finite search or numerical recognition of irrationality. No Lean proof or independent adversarial approval is claimed.

The remaining research question is the normalized global transition angle on genuinely unequal physical lattices. This result removes one exact model-to-surface shortcut while preserving that question. It gives no trace-ideal, scattering, zeta-zero or RH conclusion.
