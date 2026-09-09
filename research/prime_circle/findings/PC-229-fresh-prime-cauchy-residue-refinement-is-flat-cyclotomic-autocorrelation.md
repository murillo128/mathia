# PC-229 — fresh-prime Cauchy-residue refinement is flat cyclotomic autocorrelation

**Status:** `EXACT-DERIVED` + `LITERATURE+DERIVED` + `DECISIVE-BOUNDARY` for the squarefree-radical / packet-state continuation left open by PC-227--PC-228. PC-227 shows that, at fixed coarse conductor `N`, the fully mode-resolved fresh-prime transfer concentrates near the primitive `N`-th roots into shifted discrete Cauchy packets whose pole residue contains the exact factor

\[
\frac{1}{\alpha\Phi_N'(\alpha)},
\qquad \alpha\in P_N^*.
\]

PC-228 removes repeated-prime depth from that architecture and leaves growth of the squarefree radical as the first unclassified conductor direction. The most direct squarefree continuation is therefore to let a new prime split each primitive pole and transport this Cauchy-residue factor itself before any positive-square or packet compression.

That continuation is rigid. Under `N -> Np`, `p\nmid N`, the primitive child residues form a source-forced weighted branching operator. Its positive square is **exactly diagonal on the parent primitive roots**, with diagonal equal to a finite coefficient-autocorrelation Laurent polynomial of `Phi_N`. If `p>phi(N)`, this autocorrelation has no off-zero alias and the branching is, after one forced scalar normalization, an exact isometry. For smaller fresh primes the diagonal profile can be nonconstant, but its trace is a finite Ramanujan contraction and its determinant is an ordinary cyclotomic resultant.

More strongly, adding several distinct fresh primes produces an exactly path-independent branching system: every refinement square commutes before taking norms, and the multi-prime weight is a cubical cyclotomic coboundary. Thus the **Cauchy pole-residue subcarrier by itself** cannot create noncommuting squarefree refinement holonomy or inter-parent spectral mixing. This does not classify the complete PC-227 packet, whose numerator, rational shifts, normalization, and any source-forced operation inserted between refinement steps remain outside the result.

## 1. The PC-227 packet has an intrinsic angular pole residue

For `n>1` and a primitive root `alpha in P_n^*`, define

\[
\boxed{
\kappa_n(\alpha)
:=\frac{1}{\alpha\Phi_n'(\alpha)}.
}
\tag{1}
\]

This is not an arbitrary spectral weight. If the root is approached in angular coordinates,

\[
z=\alpha e^\varepsilon,
\]

then

\[
\Phi_n(z)
=\varepsilon\,\alpha\Phi_n'(\alpha)+O(\varepsilon^2),
\]

so `kappa_n(alpha)` is the simple-pole coefficient of `1/Phi_n` in the logarithmic/angular coordinate. It is exactly the derivative factor appearing in the Cauchy packet residue of PC-227:

\[
C_{N,r}(a,t)
=
\frac{\Phi_N(\zeta_N^{-a})}
{2\pi i\,\sqrt{H_r}}
\kappa_N(\alpha_t).
\tag{2}
\]

Thus any attempt to let the coarse squarefree conductor grow while retaining the PC-227 pole geometry must specify how the vector `kappa_N` changes under primitive-root refinement.

## 2. One fresh prime gives an exact weighted branching law

Let `p\nmid N` be prime and let `beta` be a primitive `Np`-th root. Put

\[
\alpha=\beta^p.
\]

Then `alpha` is a primitive `N`-th root. The standard fresh-prime cyclotomic recursion is

\[
\Phi_{Np}(z)=\frac{\Phi_N(z^p)}{\Phi_N(z)}.
\tag{3}
\]

At `z=beta` the numerator vanishes simply and the denominator is nonzero. Differentiating (3) therefore gives

\[
\Phi_{Np}'(\beta)
=
\frac{p\beta^{p-1}\Phi_N'(\alpha)}{\Phi_N(\beta)}.
\tag{4}
\]

Multiplication by `beta` and inversion yield the exact residue transport

\[
\boxed{
\kappa_{Np}(\beta)
=
\frac{\Phi_N(\beta)}{p}\,
\kappa_N(\beta^p).
}
\tag{5}
\]

Use ordinary counting `ell^2` on the finite primitive-root labels and define

\[
\boxed{
(B_{N,p}f)(\beta)
:=
\frac{\Phi_N(\beta)}{p}
 f(\beta^p),
\qquad \beta\in P_{Np}^*.
}
\tag{6}
\]

Then (5) is the vector identity

\[
\boxed{
\kappa_{Np}=B_{N,p}\kappa_N.
}
\tag{7}
\]

This is the canonical branching forced by the same cyclotomic recursion that generated the PC-227 fresh-prime packet; no additional kernel or gauge has been chosen.

## 3. The complete one-step singular data is coefficient autocorrelation

Fix `alpha in P_N^*`. Among the `p` solutions of

\[
\beta^p=\alpha,
\tag{8}
\]

exactly one has order `N`; it is a zero of `Phi_N`. The other `p-1` solutions are primitive of order `Np`. Consequently the missing old solution contributes zero to every squared branching weight, and the primitive-child sum may be replaced exactly by the sum over all `p` roots in (8).

Write

\[
\Phi_N(z)=\sum_{k=0}^{d}c_kz^k,
\qquad d=\varphi(N),
\qquad
h_N=\sum_{k=0}^{d}c_k^2.
\tag{9}
\]

Different parents have disjoint child fibers, so `B_{N,p}^*B_{N,p}` is diagonal. Its value at `alpha` is

\[
q_{N,p}(\alpha)
=
\frac1{p^2}
\sum_{\substack{\beta^p=\alpha\\\operatorname{ord}(\beta)=Np}}
|\Phi_N(\beta)|^2.
\tag{10}
\]

The finite root-of-unity orthogonality relation on the full fiber gives

\[
\sum_{\beta^p=\alpha}\beta^{k-\ell}
=
\begin{cases}
 p\,\alpha^{(k-\ell)/p},&p\mid k-\ell,\\
 0,&p\nmid k-\ell.
\end{cases}
\tag{11}
\]

Hence

\[
\boxed{
q_{N,p}(\alpha)
=
\frac1p
\sum_{\substack{0\le k,\ell\le d\\k\equiv\ell\pmod p}}
 c_kc_\ell\,
 \alpha^{(k-\ell)/p}.
}
\tag{12}
\]

Define the finite Laurent autocorrelation polynomial

\[
\boxed{
Q_{N,p}(z)
:=
\sum_{\substack{0\le k,\ell\le d\\k\equiv\ell\pmod p}}
 c_kc_\ell z^{(k-\ell)/p}.
}
\tag{13}
\]

Then the exact positive square is

\[
\boxed{
B_{N,p}^*B_{N,p}
=
\frac1p\,M_{Q_{N,p}|_{P_N^*}}.
}
\tag{14}
\]

Every entry in (10) is strictly positive, so `B_{N,p}` is injective. There are no hidden principal angles between different parent roots: the entire singular spectrum is the labeled scalar profile `Q_{N,p}(alpha)/p`.

A particularly strong exact threshold follows immediately. If

\[
p>d=\varphi(N),
\tag{15}
\]

then the congruence `k congruent ell (mod p)` in (13) forces `k=ell`. Therefore

\[
\boxed{
Q_{N,p}(z)=h_N,
\qquad
B_{N,p}^*B_{N,p}=\frac{h_N}{p}I.
}
\tag{16}
\]

Thus `sqrt(p/h_N) B_{N,p}` is an exact isometry whenever the new prime exceeds the coarse cyclotomic degree. If normalized counting measure is used instead on the primitive-root sets, (14)--(16) acquire only the universal additional factor `(p-1)^{-1}`; the flatness statement is unchanged.

## 4. The nonflat regime is real, but its first scalar contractions are classical

Equation (16) must not be overextended to all squarefree growth. For `p<=phi(N)`, coefficient aliases separated by multiples of `p` can survive and produce a genuinely nonconstant parent profile.

An exact control is

\[
\Phi_{15}(z)
=z^8-z^7+z^5-z^4+z^3-z+1,
\qquad h_{15}=7.
\tag{17}
\]

For the fresh prime `p=7`, the only nonzero coefficient differences divisible by `7` are `0` and `+-7`, and (13) gives

\[
\boxed{
Q_{15,7}(z)=7-2(z+z^{-1}).
}
\tag{18}
\]

Therefore, for `alpha=zeta_15^t`, `(t,15)=1`,

\[
\boxed{
q_{15,7}(\alpha)
=1-\frac47\cos\frac{2\pi t}{15}.
}
\tag{19}
\]

The squarefree residue branch is therefore not globally scalar. The exact point is narrower: its nontriviality is only a coefficient autocorrelation sampled on the existing primitive parent shell, not a new cross-parent operator.

The simplest global contractions return immediately to classical Prime-Circle arithmetic. Summing (12) over primitive roots and using the Ramanujan identity

\[
\sum_{\alpha\in P_N^*}\alpha^m=c_N(m)
\]

gives

\[
\boxed{
\operatorname{tr}(B_{N,p}^*B_{N,p})
=
\frac1p
\sum_{\substack{k\equiv\ell\pmod p}}
 c_kc_\ell\,
 c_N\!\left(\frac{k-\ell}{p}\right).
}
\tag{20}
\]

For the determinant, choose `L` so that

\[
P_{N,p}(z):=z^LQ_{N,p}(z)\in\mathbb Z[z].
\]

Because every `Q_{N,p}(alpha)` is positive, the product over primitive roots is nonzero and

\[
\boxed{
\det(B_{N,p}^*B_{N,p})
=
p^{-\varphi(N)}
\left|
\operatorname{Res}(\Phi_N,P_{N,p})
\right|.
}
\tag{21}
\]

Thus trace and determinant do not create a new zeta-bearing scalar: they reduce respectively to finite Ramanujan contraction and ordinary cyclotomic resultant data.

## 5. Fresh-prime refinement squares commute exactly

The stronger obstruction is visible before any positive square. Let `p` and `q` be distinct primes not dividing `N`, and let `gamma` be primitive of order `Npq`. Along the path `N -> Np -> Npq`, equations (6) give the total weight

\[
\frac{\Phi_{Np}(\gamma)}q
\frac{\Phi_N(\gamma^q)}p.
\tag{22}
\]

Using (3) at `gamma`,

\[
\Phi_{Np}(\gamma)
=
\frac{\Phi_N(\gamma^p)}{\Phi_N(\gamma)},
\tag{23}
\]

so (22) becomes

\[
\frac{\Phi_N(\gamma^p)\Phi_N(\gamma^q)}
{pq\,\Phi_N(\gamma)},
\tag{24}
\]

which is symmetric in `p,q`. Hence, as operators from the parent root space to the common refined root space,

\[
\boxed{
B_{Np,q}B_{N,p}
=
B_{Nq,p}B_{N,q}.
}
\tag{25}
\]

Every squarefree refinement square is therefore flat. Since any two orders of adjoining finitely many distinct primes differ by adjacent transpositions, all finite fresh-prime paths with the same endpoint give the same operator.

There is an explicit cubical formula. Let

\[
M=\prod_{j=1}^r p_j,
\qquad (M,N)=1,
\]

be squarefree, let `mathcal P={p_1,...,p_r}`, and put

\[
m_S=\prod_{p\in S}p
\qquad(S\subseteq\mathcal P).
\]

The iterated cyclotomic recursion is

\[
\Phi_{NM}(z)
=
\prod_{S\subseteq\mathcal P}
\Phi_N(z^{m_S})^{(-1)^{r-|S|}}.
\tag{26}
\]

At a primitive `NM`-th root `gamma`, only the full-set factor vanishes. Differentiating that simple zero gives the endpoint branching weight

\[
\boxed{
\frac{\kappa_{NM}(\gamma)}
{\kappa_N(\gamma^M)}
=
\frac1M
\prod_{S\subsetneq\mathcal P}
\Phi_N(\gamma^{m_S})^{(-1)^{r-1-|S|}}.
}
\tag{27}
\]

Thus the whole finite squarefree residue transport is a cyclotomic cubical coboundary. Equivalently, if `B_{N,M}` denotes the operator with weight (27) and parent map `gamma -> gamma^M`, then

\[
\boxed{
B_{NM_1,M_2}B_{N,M_1}
=B_{N,M_1M_2}
}
\tag{28}
\]

for pairwise coprime squarefree refinement factors. The final primitive children of different parent roots are still disjoint, so `B_{N,M}^*B_{N,M}` remains diagonal for every finite squarefree `M`.

The pole-residue carrier therefore has neither refinement-order holonomy nor source-forced inter-parent mixing at any finite squarefree depth.

## 6. Relation to PC-216--PC-228 and exact surviving boundary

PC-216 already found a commuting divisor-cube coboundary on the **opposite root-value orientation**: it evaluates a higher cyclotomic polynomial `Phi_{dM}` on an old primitive `d`-th root and expresses the result through finite differences of the derivative potential `zeta Phi_d'(zeta)`. PC-217 then classicalizes the surviving packetwise modulus to Dirichlet `L(1)` data.

The present calculation is distinct but strongly matched. PC-227 forces `1/(alpha Phi_N'(alpha))` as the residue of its new-prime Cauchy packets, so squarefree base growth asks how an **old denominator pole splits into new primitive preimages**. Equations (5), (14), and (25)--(28) show that this other orientation of the same cyclotomic recursion is again flat: phase/order information is a coboundary, while one-step metric information is only coefficient autocorrelation.

Combined with PC-228, the boundary is now sharper. Repeated-prime depth contributes only radical dilation/aliasing, and the most literal pole-residue continuation along new squarefree directions contributes only a flat weighted branching forest. Therefore the route

\[
\boxed{
\text{PC-227 Cauchy pole residue}
\to
\text{grow squarefree radical by primitive preimages}
\to
\text{refinement holonomy / inter-parent spectrum}
\to
\text{new RH mechanism}
}
\]

is closed at this canonical level.

This finding does **not** close the full simultaneous squarefree-base/fresh-prime problem. In particular it does not classify:

- the numerator `Phi_N(zeta_N^{-a})`, rational packet shift `sigma`, or residue-class normalization `H_r` in the complete PC-227 packet;
- an intrinsic operator inserted between branching steps that mixes different parent fibers before the next refinement;
- the nonconstant autocorrelation profiles (13) in a simultaneous regime with `N -> infinity` and fresh primes `p<=phi(N)`;
- a collective invariant coupling several conductor packets, or the global uniformization/accessory-parameter sector.

Those are genuine surviving routes. What is no longer available is the claim that the Cauchy derivative residue itself creates a new noncommutative squarefree transport merely because the number of primitive roots grows.

## 7. Prior-art and novelty audit

The algebraic ingredients are classical. The prime-extension recursion (3) is standard cyclotomic theory. Bartlomiej Bzdega, Andres Herrera-Poyatos and Pieter Moree, **Cyclotomic polynomials at roots of unity**, *Acta Arithmetica* 184 (2018), 215--230, DOI `10.4064/aa170112-20-12`, study cyclotomic values and logarithmic derivatives at roots of unity by finite Fourier methods and give a short resultant derivation; PC-216 already uses this work as the direct root-value boundary. Carlo Sanna's 2022 cyclotomic-coefficient survey already anchored in `research/prime_circle/SOURCES.md` is the broad boundary for the coefficient data in (9)--(19). Ramanujan sums and Apostol's cyclotomic resultant theorem are also existing source anchors for (20)--(21).

Finite-fiber Parseval in (11) and the fact that a weighted map with disjoint fibers has diagonal positive square are generic harmonic/linear-algebra facts. The `p>deg Phi_N` threshold is consequently an elementary no-alias statement, not a novel theorem about cyclotomic coefficients.

A directed literature search around cyclotomic derivative residues, primitive-root preimage branching, coefficient autocorrelation, and barycentric weights did not locate an independent RH or spectral mechanism containing the exact PC-227 organization above. That absence is not used to claim historical novelty. The durable content is the **Prime-Circle scope classification**: the specific Cauchy-residue state left by PC-227 remains a flat cyclotomic branching system under the first squarefree-radical continuation, and its one-step metric defect is explicitly finite coefficient autocorrelation rather than a new spectral carrier.

## 8. Audit / falsification tests

1. For any `p\nmid N` and primitive `beta` of order `Np`, differentiate (3) and verify (5) exactly.
2. For each primitive parent `alpha`, enumerate its `p` preimages and verify that one old preimage has zero weight while (12)--(14) reproduce the primitive-child norm.
3. If `p>phi(N)`, verify that all off-zero coefficient aliases disappear and (16) holds exactly.
4. For `(N,p)=(15,7)`, expand `Phi_15` and check (18)--(19); this falsifies any stronger claim that every fresh-prime step is scalar.
5. For distinct fresh primes `p,q`, compare both two-step weights at every primitive `Npq` root and verify the commuting square (25).
6. Multiply (26) through a primitive endpoint root, differentiate its unique vanishing full-set factor, and verify the cubical endpoint ratio (27).
7. Compare the trace and determinant of the explicit diagonal matrix (14) against (20) and (21).

Any failure of the derivative branching identity, appearance of a cross-parent matrix element in the positive square, nonflatness above the no-alias threshold, or nontrivial refinement-order holonomy would falsify this classification.