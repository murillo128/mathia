# PC-368 — heterogeneous Fock channels retain resonant word contractions beyond homogeneous Gram data

- **Finding ID:** `PC-368`
- **Status:** `EXACT-DERIVED` + `LITERATURE+DERIVED` + `DECISIVE-BOUNDARY`
- **Status detail:** exact boundary for the mixed-degree/nontriangular full-Fock escape left open by PC-367. Heterogeneous tensor degrees genuinely retain cross-grade tensor information through equal-total-grade word resonances, so the homogeneous Gram collapse does not extend verbatim. However every such resonant word-Gram invariant is preserved by a common one-particle unitary and therefore by the exact Prime-Circle matched-control parity of PC-355. Mixed degree is an information-preserving mechanism, but these canonical contraction invariants alone are not an arithmetic or RH selector.
- **Workflow:** `DERIVED + PRIOR-ART AUDIT + ADVERSARIAL CONTROL`
- **Research line:** `prime_circle`
- **Result type:** exact graded operator-theoretic boundary / cross-grade information-retention theorem
- **RH relevance:** high as a frontier clarification. PC-367's same-degree Wold/Gram no-go has a real mixed-degree escape, but the first exact invariants carried by that escape remain control-blind under the source-native parity already identified in PC-355.

## Claim

PC-367 classifies any finite family of full-Fock left creators whose source tensors all have one common degree: together with tensor grade, their complete joint unitary type retains only the finite channel Gram matrix. Its boundary explicitly leaves open heterogeneous degrees, because different channel words can then reach the same Fock grade by different degree partitions.

That distinction is substantive and exact.

Let `K` be a finite-dimensional complex Hilbert space and

\[
\mathcal F(K)=\bigoplus_{n\ge0}K^{\otimes n},
\qquad
N|_{K^{\otimes n}}=nI.
\tag{1}
\]

For labelled tensors

\[
g_i\in K^{\otimes q_i},\qquad q_i\ge1,
\tag{2}
\]

write `L_i=L_{g_i}` for left creation,

\[
L_{g_i}\xi=g_i\otimes\xi.
\tag{3}
\]

For a channel word `alpha=(i_1,...,i_r)` define

\[
g_\alpha:=g_{i_1}\otimes\cdots\otimes g_{i_r},
\qquad
Q(\alpha):=q_{i_1}+\cdots+q_{i_r}.
\tag{4}
\]

Then

\[
L_\alpha:=L_{i_1}\cdots L_{i_r}=L_{g_\alpha}.
\tag{5}
\]

Using the Hilbert inner product convention linear in the second argument, equal total grade gives the exact scalar relation

\[
\boxed{
Q(\alpha)=Q(\beta)
\quad\Longrightarrow\quad
L_\alpha^*L_\beta
=\langle g_\alpha,g_\beta\rangle I.
}
\tag{6}
\]

Thus the graded operator tuple `(N,L_1,...,L_m)` necessarily retains every **resonant word-Gram invariant**

\[
\boxed{
R_{\alpha,\beta}
:=\langle g_\alpha,g_\beta\rangle,
\qquad Q(\alpha)=Q(\beta).
}
\tag{7}
\]

When all `q_i` are equal, these invariants factor completely through the degree-one channel Gram matrix and PC-367 is recovered. When the `q_i` differ, equal total grade can occur for words of different lengths, and (7) contains genuinely new cross-grade tensor contractions not determined by the separate same-degree Gram data.

For two channels `g in K^{otimes p}` and `h in K^{otimes q}`, put

\[
d=\gcd(p,q),\qquad
a=q/d,\qquad b=p/d.
\tag{8}
\]

The first unavoidable arithmetic resonance between their degree semigroups occurs at `lcm(p,q)=ap=bq`, and the tuple retains

\[
\boxed{
R_{p,q}(g,h)
=\left\langle g^{\otimes a},h^{\otimes b}\right\rangle,
\qquad
(L_g^a)^*L_h^b=R_{p,q}(g,h)I.
}
\tag{9}
\]

This scalar can vary while all individual channel norms and all within-degree Gram data remain fixed. Therefore PC-367's homogeneous Gram classification does **not** extend to heterogeneous channels by simply taking a disjoint Gram matrix degree by degree.

At the same time, (7) is invariant under every common one-particle unitary `J`: replacing each `g_i` by `J^{otimes q_i}g_i` sends both resonant words to the same `J^{otimes Q(alpha)}` image. Hence

\[
\boxed{
\widetilde R_{\alpha,\beta}=R_{\alpha,\beta}
}
\tag{10}
\]

for all equal-total-grade words. In particular, the source/control parity of PC-355 preserves the complete resonant word-Gram system. Mixed degree therefore retains more tensor information than PC-367, but this canonical contraction package does not break the matched non-arithmetic control.

## 1. Unequal degrees leave residual prefix contractions

The basic distinction already appears before closing a resonance. If

\[
g\in K^{\otimes p},\qquad h\in K^{\otimes q},\qquad p<q,
\tag{11}
\]

then `L_g^*L_h` is no longer a scalar. Contract the first `p` tensor slots of `h` against `g`, obtaining

\[
C_g h\in K^{\otimes(q-p)}.
\tag{12}
\]

Directly from the tensor-product inner product,

\[
\boxed{
L_g^*L_h=L_{C_g h}.
}
\tag{13}
\]

For equal degrees the residual tensor sector has degree zero and (13) reduces to the scalar Gram relation used throughout PC-367. For unequal degrees, however, the adjoint product remains a nontrivial creator. Repeated compositions of such prefix contractions eventually close whenever two channel words have equal weighted degree, yielding (6).

This identifies precisely where the homogeneous Wold gauge stops being sufficient: it can erase orientation inside one fixed tensor sector while preserving its Gram matrix, but heterogeneous channels impose compatibility between **different tensor factorizations of the same total grade**.

## 2. Why the homogeneous case contains no such extra data

Suppose every channel has one common degree `q`. Then

\[
Q(\alpha)=Q(\beta)
\quad\Longleftrightarrow\quad
|\alpha|=|\beta|.
\tag{14}
\]

For words of equal length `r`, tensor-product factorization gives

\[
\langle g_\alpha,g_\beta\rangle
=
\prod_{k=1}^{r}
\langle g_{i_k},g_{j_k}\rangle.
\tag{15}
\]

Every resonant word invariant is therefore a monomial in the ordinary channel Gram entries. Nothing beyond the finite matrix

\[
G_{ij}=\langle g_i,g_j\rangle
\tag{16}
\]

is generated. This is exactly compatible with PC-367's complete homogeneous classification.

Heterogeneous degree changes (14). A word of one length can collide in total grade with a word of another length, so (15) no longer reduces the comparison to aligned pairwise channel inner products. The new datum is not merely “more channels”; it is **multiple factorizations of one Fock grade**.

## 3. Minimal exact counterexample to homogeneous Gram collapse

Take

\[
K=\mathbb C^2,
\qquad e_0,e_1\text{ orthonormal}.
\tag{17}
\]

Compare the two labelled mixed-degree systems

\[
\begin{aligned}
\text{A: }&g=e_0\in K,
&h=e_0\otimes e_0\in K^{\otimes2},\\
\text{B: }&g'=e_0\in K,
&h'=e_1\otimes e_0\in K^{\otimes2}.
\end{aligned}
\tag{18}
\]

Both have exactly the same individual degree labels and norms,

\[
\|g\|=\|g'\|=\|h\|=\|h'\|=1.
\tag{19}
\]

Since there is only one channel in each degree, their separate within-degree Gram data are identical. Yet the first degree-two resonance is

\[
\langle g\otimes g,h\rangle=1,
\qquad
\langle g'\otimes g',h'\rangle=0.
\tag{20}
\]

Equivalently,

\[
(L_g^2)^*L_h=I,
\qquad
(L_{g'}^2)^*L_{h'}=0.
\tag{21}
\]

So the two mixed-degree tuples cannot be jointly unitarily equivalent. This is an exact finite counterexample to any attempted extension of PC-367 that classifies heterogeneous channels using only the Gram matrix inside each homogeneous degree.

## 4. A canonical pointed spectral moment sees the first resonance

The extra information is not confined to an abstract nonselfadjoint word relation. For the `1:2` resonance define the bounded selfadjoint Fock operator

\[
A:=L_g+L_g^*+L_h+L_h^*.
\tag{22}
\]

Let `Omega` be the Fock vacuum. In three applications of `A`, the only grade-compatible closed paths from grade zero are

\[
0\to1\to2\to0
\quad\text{and}\quad
0\to2\to1\to0.
\tag{23}
\]

Consequently

\[
\boxed{
\langle\Omega,A^3\Omega\rangle
=2\operatorname{Re}\langle h,g\otimes g\rangle.
}
\tag{24}
\]

For the systems in (18), this vacuum third moment is respectively `2` and `0`. Thus the canonical pointed spectral measure of `A` at the vacuum distinguishes the two systems.

If `N` is retained, the vacuum is not an arbitrary observer: it spans the unique grade-zero eigenspace of `N`. Any unitary intertwining the graded tuples preserves that line, so its spectral moments are genuine invariants of the construction.

Equation (24) is deliberately modest. It does **not** claim that the ordinary global spectrum of one scalar Hamiltonian is a complete mixed-degree invariant. It proves only what is needed for the boundary: cross-grade resonance can survive into a canonical selfadjoint spectral readout, whereas the homogeneous families of PC-366/PC-367 collapse to norm/Gram data.

## 5. Application to the Prime-Circle inversion tensor tower

PC-349/PC-350 produce a source-native completed tensor object from the reciprocity-closed Prime-Circle radial path. Write its homogeneous expansion schematically as

\[
\mathcal D_S=1+d_1+d_2+d_3+\cdots,
\qquad d_q\in K_S^{\otimes q}.
\tag{25}
\]

For the closed inversion defect, PC-349 gives `d_1=0`; PC-350 shows that unbounded tensor depth is nevertheless faithful to the centered source profile. PC-355 then studies the canonical full-Fock realization of the whole series, while PC-366/PC-367 isolate homogeneous creator channels and prove their norm/Gram collapses.

The present result locates the exact information that homogeneous isolation discards. If two nonzero tensor levels `d_p,d_q` are retained simultaneously, the graded creator tuple contains the resonances

\[
\left\langle
 d_p^{\otimes(q/d)},
 d_q^{\otimes(p/d)}
\right\rangle,
\qquad d=\gcd(p,q),
\tag{26}
\]

and, with multiple channels per level, the more general equal-total-grade word Gram system (7). These quantities compare different partitions of a common tensor degree and therefore are not recoverable from the separate homogeneous Gram matrices in general.

For the inversion defect, the first structurally natural `2:4` example, whenever both levels are present, is

\[
\boxed{
R_{2,4}
=\langle d_2\otimes d_2,d_4\rangle.
}
\tag{27}
\]

No claim is made here that (27) is nonzero for every shell set, nor that it already contains new arithmetic. The exact statement is that heterogeneous full-Fock coupling has access to this source-native cross-level contraction and PC-367's same-degree classification does not erase it.

## 6. The matched-control parity still survives every resonance

The decisive RH-facing control comes from PC-355. In the centered Prime-Circle alphabet, the matched reciprocal control is obtained by one unitary involution `J` on the one-particle space, and each homogeneous tensor transforms as

\[
\widetilde d_q=J^{\otimes q}d_q.
\tag{28}
\]

For a channel word of total grade `Q`,

\[
\widetilde g_\alpha
=J^{\otimes Q}g_\alpha.
\tag{29}
\]

Therefore every resonance satisfies

\[
\begin{aligned}
\widetilde R_{\alpha,\beta}
&=\langle J^{\otimes Q}g_\alpha,
          J^{\otimes Q}g_\beta\rangle\\
&=\langle g_\alpha,g_\beta\rangle
=R_{\alpha,\beta}.
\end{aligned}
\tag{30}
\]

This is not special to parity: it holds for any common one-particle unitary. For the specific Prime-Circle control it means that even though mixed degree repairs the **information loss** exposed by PC-367, its canonical resonant contractions do not repair the **arithmetic discrimination failure** exposed by PC-355.

The distinction matters. “Mixed degree retains more information” is true; “therefore mixed degree supplies a zeta/RH spectral mechanism” does not follow. Any RH-facing continuation has to identify a source-forced cross-level structure that is not merely a common-unitary invariant of tensor words, or else provide an independent theorem showing why a control-blind invariant is still sufficient for the target.

## 7. Prior-art and novelty audit

The abstract Fock-space ingredients are classical and no historical novelty is claimed for them. Full Fock space and left creation operators are the standard free-semigroup/Cuntz--Toeplitz model. Gelu Popescu's work on noncommuting operator tuples and Fock-space multi-analytic operators, including **Isometric dilations for infinite sequences of noncommuting operators**, *Transactions of the AMS* 316:2 (1989), 523--536, and **Multi-analytic operators on Fock spaces**, *Mathematische Annalen* 303 (1995), 31--46, is foundational. Davidson and Pitts, **Invariant Subspaces and Hyper-Reflexivity for Free Semigroup Algebras**, *Proceedings of the London Mathematical Society* 78 (1999), 401--430, develops the left-regular free-semigroup algebra generated by the canonical shifts. In that standard word model, prefix cancellation and the scalar equal-length relation behind (6) are basic operator algebra.

The tensor-series/Fock interpretation of path signatures is also established prior art. Kiraly and Oberhauser, **Kernels for Sequentially Ordered Data**, *JMLR* 20:31 (2019), 1--45, and the broader signature literature treat iterated-integral tensor series as Hilbert/tensor feature objects. PC-355 already anchored the Prime-Circle use of that framework and proved the stronger matched-control unitary equivalence of the canonical full-Fock realization.

A targeted search of Fock/free-semigroup operator theory, path-signature Hilbertizations, and zeta/RH spectral constructions found no basis for claiming the operator identity (6), prefix contraction (13), or mixed weighted-degree resonance as new general mathematics. The line-local delta is narrower: **PC-367's homogeneous Gram collapse has a precise failure mode at weighted-degree resonances, but every such canonical word-Gram invariant remains inside PC-355's common-unitary matched-control obstruction.** This is a boundary classification, not a new zeta representation.

## 8. Adversarial / falsification audit

- **Equal-degree control:** when all `q_i=q`, equal total grade forces equal word length and (15) reduces every resonance to products of the ordinary channel Gram entries. The result therefore agrees exactly with PC-367 rather than contradicting it.
- **Unequal-degree control:** for `p<q`, direct action on elementary tensors gives `L_g^*L_h=L_{C_g h}`. No spectral theorem or Wold assumption is used to obtain the residual tensor.
- **Closure control:** when weighted word degrees agree, the residual degree is zero, so the adjoint product is exactly scalar and yields (6).
- **Explicit counterexample:** the two systems in (18) have identical degree labels and separate within-degree Gram data but resonance `1` versus `0`; any proposed heterogeneous classification by those separate Grams is therefore false.
- **Vacuum-moment check:** in (24), all three-step words except the two grade paths in (23) annihilate the vacuum or finish in positive grade. The surviving amplitudes are conjugates, yielding exactly twice the real part.
- **Gauge control:** a common one-particle unitary acts as the same `J^{otimes Q}` on both sides of every equal-grade word comparison, proving (30). No choice of basis can turn the resonant Gram system into a parity-breaking invariant.
- **Prime-Circle control:** the application uses only homogeneous pieces already forced by the inversion defect. No external channel tensor is inserted. Conversely, no nonvanishing or zero-sensitive property of (26)/(27) is assumed without proof.
- **RH wrapper test:** the construction introduces no spectral parameter `s`, gamma factor, functional equation, zero condition, positivity theorem, or critical-line selector. The mere existence of a nontrivial vacuum moment is not counted as RH progress.

## Boundary assessment

PC-367 closes the finite **same-degree** multichannel Fock escape by proving that only the channel Gram matrix survives. PC-368 shows that the restriction to one common degree is essential: heterogeneous channels have weighted-degree resonances, and those resonances preserve real cross-level tensor information. The smallest `1:2` example already reaches a canonical selfadjoint vacuum spectral moment.

But this does not reopen the cheap Fock spectralization rejected by PC-355. All resonant word-Gram data are invariant under the exact Prime-Circle source/control parity, indeed under any common one-particle unitary. The surviving frontier is therefore narrower than “try mixed degrees”: one needs a **source-forced cross-level operation not reducible to common-unitary word contractions**, or an independently justified arithmetic bridge that makes a control-invariant quantity target-sensitive.

Single durable finding. No clue disposition is changed. The literature anchors delimit the classical Fock/free-semigroup mechanism; the Prime-Circle-specific mixed-degree boundary is derived explicitly above, so no separate `SOURCES.md` edit is required.