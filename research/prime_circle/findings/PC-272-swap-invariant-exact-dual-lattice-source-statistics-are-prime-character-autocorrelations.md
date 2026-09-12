# PC-272 — swap-invariant exact dual-lattice source statistics are prime-character autocorrelations

**Status:** `EXACT-DERIVED` + `PRIOR-ART-CLASSICALIZATION` + `DECISIVE-BOUNDARY` for the fixed-upper exact-lattice statistics left open by PC-271.

PC-271 left open whether the arithmetic distribution of the exact dual lattice

\[
\Lambda_{p,r;q}=\{(h,k)\in\mathbb Z^2:hp+kr\equiv0\pmod q\}
\]

along prime triples could carry source-specific information beyond the universal geometry-of-numbers bounds. For a fixed prime upper level `q`, that question has an exact multiplicative reduction.

Let

\[
P_q:=\{\ell:\ell\text{ prime},\ 2<\ell<q\},
\qquad M_q:=|P_q|,
\]

and, for `p,r in P_q`, put

\[
a:=pr^{-1}\pmod q\in G_q:=(\mathbb Z/q\mathbb Z)^\times.
\]

Then

\[
\boxed{
\Lambda_{p,r;q}
=
\Lambda_q(a)
:=\{(h,k)\in\mathbb Z^2:ha+k\equiv0\pmod q\}.
}
\tag{1}
\]

Consequently every statistic of the **exact** lattice that is invariant under common rescaling of `(p,r)` factors through the ratio `a`. In particular the PC-271 systole `lambda_{p,r;q}` and every coordinate-swap-invariant shape functional of the full lattice are functions of `a` alone. The complete `q`-point torus orbit also has the exact set representation

\[
\left\{\left(\left\{\frac{up}{q}\right\},\left\{\frac{ur}{q}\right\}\right):u\bmod q\right\}
=
\left\{\left(\left\{\frac{va}{q}\right\},\frac vq\right):v\bmod q\right\}.
\tag{2}
\]

The prime-source law of this quotient is not a new spectral distribution: its multiplicative Fourier transform is exactly the power spectrum of the classical prime character sums

\[
A_q(\chi):=\sum_{p\in P_q}\chi(p).
\]

More precisely, if

\[
\mu_q(a)
:=\frac1{M_q^2}
\#\{(p,r)\in P_q^2:pr^{-1}\equiv a\pmod q\},
\tag{3}
\]

then for every Dirichlet character `chi mod q`,

\[
\boxed{
\sum_{a\in G_q}\mu_q(a)\chi(a)
=
\frac{|A_q(\chi)|^2}{M_q^2}.
}
\tag{4}
\]

Thus the fixed-upper exact-lattice source statistics left open in PC-271 are precisely multiplicative autocorrelation data of the prime residue set. This is a substantive boundary, not a new RH mechanism: any critical-line sensitivity entering this packet is inherited from classical character sums over primes and hence from Dirichlet `L(s,chi)` theory. The genuinely mesoscopic ordered-time quantity `Delta_B(p,r;q)` of PC-271 does **not** factor through `a`; that distinction leaves the near-resonance/partial-window branch open.

## 1. Exact quotient reduction

Because `r` is invertible modulo the prime `q`, multiplying the defining congruence for `Lambda_{p,r;q}` by `r^{-1}` gives

\[
hpr^{-1}+k\equiv0\pmod q,
\]

which proves (1). The full-orbit reduction (2) follows by the bijective reindexing `v=ur mod q`.

The PC-271 systole therefore has the form

\[
\lambda_{p,r;q}=\lambda_q(a),
\qquad
\lambda_q(a)
:=\min_{(h,k)\in\Lambda_q(a)\setminus\{0\}}\max(|h|,|k|).
\tag{5}
\]

Moreover

\[
\Lambda_q(a^{-1})
\]

is obtained from `Lambda_q(a)` by swapping the two coordinates. Hence

\[
\boxed{\lambda_q(a^{-1})=\lambda_q(a).}
\tag{6}
\]

The same holds for every exact-lattice observable `F` invariant under coordinate swap. This is exactly the symmetry needed to pass from ordered prime pairs to the canonical source ordering `p<r` without losing information for that class of observables.

## 2. The source measure is a character autocorrelation

For a multiplicative character `chi` of `G_q`, unitarity gives

\[
\chi(pr^{-1})=\chi(p)\overline{\chi(r)}.
\]

Therefore

\[
\begin{aligned}
\sum_{a\in G_q}\mu_q(a)\chi(a)
&=\frac1{M_q^2}\sum_{p,r\in P_q}\chi(pr^{-1})\\
&=\frac1{M_q^2}
\left(\sum_{p\in P_q}\chi(p)\right)
\overline{\left(\sum_{r\in P_q}\chi(r)\right)}\\
&=\frac{|A_q(\chi)|^2}{M_q^2},
\end{aligned}
\]

which is (4).

Equivalently, for any `F:G_q -> C`, define the normalized multiplicative Fourier coefficient

\[
\widehat F(\chi)
:=\frac1{q-1}\sum_{a\in G_q}F(a)\overline{\chi(a)}.
\tag{7}
\]

Fourier inversion and (4) give the exact source average

\[
\boxed{
\frac1{M_q^2}\sum_{p,r\in P_q}F(pr^{-1})
=
\sum_{\chi\bmod q}\widehat F(\chi)
\frac{|A_q(\chi)|^2}{M_q^2}.
}
\tag{8}
\]

The principal-character term is just the uniform average of `F` on `G_q`. Every deviation from that matched uniform residue control is carried by the nonprincipal character powers `|A_q(chi)|^2`.

For distinct ordered pairs, remove the diagonal `p=r`. Since every character equals one at the identity,

\[
\boxed{
\sum_{a\in G_q}\mu_q^{\ne}(a)\chi(a)
=
\frac{|A_q(\chi)|^2-M_q}{M_q(M_q-1)}.
}
\tag{9}
\]

If `F(a)=F(a^{-1})`, then swapping `(p,r)` does not change `F`; hence the canonical unordered source average satisfies

\[
\boxed{
\frac{2}{M_q(M_q-1)}\sum_{p<r\atop p,r\in P_q}F(pr^{-1})
=
\sum_{\chi\bmod q}\widehat F(\chi)
\frac{|A_q(\chi)|^2-M_q}{M_q(M_q-1)}.
}
\tag{10}
\]

Taking `F=lambda_q`, or any coordinate-swap-invariant exact-lattice shape statistic, therefore reduces its complete fixed-`q` prime-source law to this classical character-power packet.

## 3. A translation gauge exposes the information loss

The quotient carrier has an exact gauge. For any `c in G_q`, replace an arbitrary residue source set `S subset G_q` by its common multiplicative translate `cS`. Then

\[
(cs_1)(cs_2)^{-1}=s_1s_2^{-1},
\tag{11}
\]

so its entire ratio multiset, every exact lattice `Lambda_q(s_1s_2^{-1})`, and every ratio-only observable are unchanged.

On the character side,

\[
A_{cS}(\chi)=\chi(c)A_S(\chi),
\qquad
|A_{cS}(\chi)|^2=|A_S(\chi)|^2.
\tag{12}
\]

Thus this carrier sees the multiplicative **autocorrelation/power spectrum** of the source but discards the common multiplicative phase/placement. This is the finite-group analogue of the standard phase-loss/homometry phenomenon. It is a useful matched-control boundary: any proposed prime discriminator built only from the fixed-upper exact lattice cannot recover source information erased by (11).

This statement does not assert that every translated residue set corresponds to a valid family of prime or composite polygon conductors. It identifies the exact information quotient of the lattice carrier itself.

## 4. Critical-line content is inherited Dirichlet-`L` data

The quantities `A_q(chi)` are ordinary character sums over primes (with the single prime `2` omitted here to match the source convention). Their cancellation is classical analytic-number-theory data controlled by zeros of Dirichlet `L(s,chi)`.

For example, Pilatte's Proposition 3.9 gives prime-character cancellation from a zero-free rectangle for `L(s,chi)` and states explicitly that the bound is a standard consequence of the explicit formula; under GRH it yields almost square-root cancellation. Matomäki--Teräväinen likewise reduce product-of-primes residue questions to multiplicative character sums.

Therefore the route

\[
\text{fixed upper prime source}
\longrightarrow
\text{exact dual-lattice statistic}
\longrightarrow
\text{character decomposition}
\]

lands exactly in the established Dirichlet-character/Dirichlet-`L` package. A statistic such as `lambda_q(a)` can weight the characters in (8), but the source-dependent coefficients remain `|A_q(chi)|^2`; no new zeta spectral parameter or independent critical-line operator is produced by this reduction. In addition, squaring discards the phase of each character sum.

This does **not** establish a no-go for every use of these lattices. It classicalizes the source distribution of fixed-upper, ratio-only exact-lattice observables. Any stronger claim must use information not contained in this autocorrelation packet.

## 5. Sharp boundary: `Delta_B` does not factor through the quotient

PC-271's mesoscopic quantity is

\[
\Delta_B(p,r;q)
=
\min_{0<\max(|h|,|k|)\le B}
\left\|\frac{hp+kr}{q}\right\|_{\mathbb R/\mathbb Z}.
\tag{13}
\]

Although

\[
hp+kr\equiv r(ha+k)\pmod q,
\tag{14}
\]

multiplication by the unit `r` does not preserve the least-residue distance to zero on `R/Z`. Consequently `Delta_B` is not determined by `a=pr^{-1}`.

An admissible prime-source control is `q=13`, `B=1`. Both pairs

\[
(p,r)=(3,5),\qquad (p',r')=(7,3)
\]

lie in `P_{13}^2` and have the same quotient,

\[
3\,5^{-1}\equiv3\cdot8\equiv11\pmod{13},\qquad
7\,3^{-1}\equiv7\cdot9\equiv11\pmod{13}.
\]

For `B=1`, the eight nonzero vectors in the unit sup-norm box reduce the least circular residue search to the classes `±p`, `±r`, and `±p±r`. For `(3,5)` the minimum distance to `0 mod 13` is `2`, attained by `-3+5`; for `(7,3)` the minimum is `3`, attained by `±3` (also `7+3=10` has circular distance `3`). Hence

\[
\boxed{
\Delta_1(3,5;13)=\frac2{13},
\qquad
\Delta_1(7,3;13)=\frac3{13}.
}
\tag{15}
\]

Thus `Delta_B` fails to factor through the quotient even after restricting to the actual prime source `P_q^2`, not merely on the ambient set of nonzero residue pairs.

The same warning applies to orientation-sensitive shortest-vector data when one imposes the canonical order `p<r`: inversion `a <-> a^{-1}` swaps coordinates, so only inversion/swap-invariant observables admit the clean unordered formula (10).

Thus PC-272 closes a specific part of PC-271's frontier while leaving its genuinely ordered mesoscopic branch intact. Near-resonance time, partial collision windows, and observables coupling the raw orbit order to source-forced transfer remain legitimate targets precisely because they retain the scaling information erased by the quotient lattice.

## 6. Prior-art and novelty audit

The harmonic identity (4) is standard finite-abelian-group Fourier analysis: ratio counts are a multiplicative autocorrelation and their Fourier transform is a squared Fourier magnitude. The prime-specific coefficients are standard character sums over primes.

Kaisa Matomäki and Joni Teräväinen, **Products of primes in arithmetic progressions**, *Journal für die reine und angewandte Mathematik (Crelles Journal)* 2024, no. 808 (2024), 193--240, DOI `10.1515/crelle-2023-0096`, arXiv `2301.07679`, provide a close modern arithmetic reference: residue classes represented by products of primes are analyzed through multiplicative characters and character sums over primes.

Cédric Pilatte, **Unconditional correctness of recent quantum algorithms for factoring and computing discrete logarithms**, *Forum of Mathematics, Pi* 14 (2026), e5, DOI `10.1017/fmp.2025.10023`, gives in Proposition 3.9 a prime-character-sum bound from a zero-free region of `L(s,chi)`, derives it from the explicit formula in Appendix A, and notes the near square-root cancellation supplied by GRH.

No novelty is claimed for multiplicative Fourier inversion, autocorrelation/power-spectrum duality, or the connection between prime character sums and Dirichlet `L`-functions. The project-local contribution is narrower and exact: the source-statistics escape explicitly left open by PC-271 for the **fixed-upper exact lattice and full orbit** factors through the prime-ratio autocorrelation, while the PC-271 inverse-near-resonance observable provably does not. This separates a classicalized branch from a still-live one without conflating the two.

## 7. Falsification and audit tests

The reduction has direct finite checks.

1. For any prime `q`, enumerate `P_q`, form the ratio histogram (3), and compare every multiplicative-character moment with (4).
2. Compute `lambda_q(a)` by exact lattice search and compare the direct prime-pair average with the character expansion (8) or, for canonical `p<r`, with (10).
3. Multiply an arbitrary residue source set by a fixed unit `c`; the ratio histogram and every ratio-only exact-lattice statistic must remain unchanged while each character sum acquires the phase `chi(c)`.
4. The explicit prime-source `q=13`, `B=1` control in (15) must distinguish the two admissible representatives `(3,5)` and `(7,3)` with the same quotient `a=11`; failure would contradict the stated boundary between exact-lattice and mesoscopic ordered-time data.
5. Any claimed fixed-upper exact-lattice prime discriminator should be tested against residue-source controls with the same multiplicative autocorrelation. If it distinguishes such controls while using only ratio-lattice data, the observable has been specified incorrectly or contains additional information not accounted for here.

## 8. Consequences for the research line

PC-271 asked whether prime-specific statistics of `lambda`, `Delta_B`, shortest directions, or couplings to nonlocal transfer could beat the classical rank-one-lattice carrier. PC-272 gives a split answer.

For `lambda` and every swap-invariant statistic of the exact lattice/full orbit, the prime-source weighting is completely classified by the multiplicative character powers `|A_q(chi)|^2`. Any RH sensitivity here is inherited Dirichlet-`L`/GRH character-sum information and additionally suffers a phase-loss quotient. This branch should not be treated as a new prime-circle spectral mechanism without extra structure.

By contrast, `Delta_B`, partial-window dynamics, orientation-sensitive data, and observables coupling raw orbit order to geometry are not captured by the ratio autocorrelation. They remain the mathematically honest continuation of the PC-271 frontier, subject to matched controls and a fresh prior-art audit before any RH claim.