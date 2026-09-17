# AF-398 — Prime PF3 successor wall has a third-scale log-log correction

## Status

`EXACT-DERIVED` · `LITERATURE+DERIVED` · `ARITHMETIC-FIDELITY` · `TARGET-FIDELITY` · `TOTAL-POSITIVITY` · `PF3` · `PRIME-LOGS` · `LOCAL-TO-GLOBAL` · `BOUNDARY-TOPOLOGY` · `QUANTITATIVE-SAMPLING` · `NEGATIVE/OBSTRUCTION` · `NO-NOVELTY-CLAIM`

## Claim

AF-397 resolves the prime-log PF3 successor threshold through the scale `N/log N` and leaves the boundary family

\[
R_N=(e-1)N-e\frac{N}{\log N}+o\!\left(\frac{N}{\log N}\right)
\]

open. The next correction is forced by the classical logarithmic variation of the `n`th prime.

Write

\[
L=\log N,
\qquad
\ell=\log L,
\qquad
e_n=\log p_n,
\]

and for fixed `\beta\in\mathbb R` define

\[
R_N(\beta)
=
\left\lfloor
(e-1)N-e\frac{N}{L}
+\beta\frac{N\ell}{L^2}
\right\rfloor.
\tag{1}
\]

For the AF-395 two-component curvature profile, let

\[
H_N(R)=e_{N+R}-e_N
      =\log\frac{p_{N+R}}{p_N}
\tag{2}
\]

and

\[
\Delta_N(R)
=
\max_{N\le n<N+R}(e_{n+1}-e_n).
\tag{3}
\]

Then

\[
H_N(R_N(\beta))
=
1+
\left(\frac{\beta}{e}-1\right)
\frac{\ell}{L^2}
+O\!\left(\frac{\ell^2}{L^3}\right).
\tag{4}
\]

Consequently:

- if `\beta<e`, every sampled `3\times3` minor whose six indices lie in `[N,N+R_N(\beta)]` is nonnegative for all sufficiently large `N`;
- if `\beta>e`, every sufficiently large block `[N,N+R_N(\beta)]` contains a strictly negative sampled `3\times3` minor.

Thus the second-order boundary of AF-397 splits one scale further:

\[
\boxed{
R_N^{\mathrm{crit}}
=
(e-1)N
-e\frac{N}{\log N}
+e\frac{N\log\log N}{\log^2N}
+O\!\left(
\frac{N(\log\log N)^2}{\log^3N}
\right)
}
\tag{5}
\]

in the same one-sided detection sense as AF-397.

Equivalently, the exact physical locality-wall count

\[
B_N=\pi(e p_N)-N
\tag{6}
\]

satisfies

\[
B_N
=
(e-1)N
-e\frac{N}{L}
+e\frac{N\ell}{L^2}
+O\!\left(\frac{N\ell^2}{L^3}\right).
\tag{7}
\]

AF-397 therefore did not merely leave an unspecified lower-order ambiguity at `\alpha=e`: the next resource term is positive and of size `eN\log\log N/\log^2N`. The unresolved boundary is now thinner, at scale `N(\log\log N)^2/\log^3N` and below.

## Third-scale conversion from prime index to physical reach

Use the classical Cipolla expansion in the form

\[
p_n
=
n\left(
\log n+\log\log n-1
+\frac{\log\log n-2}{\log n}
+O\!\left(\frac{(\log\log n)^2}{\log^2n}\right)
\right).
\tag{8}
\]

This is a low-order specialization of the full expansion audited in AF-397. Write

\[
A(n)=\frac{p_n}{n}.
\tag{9}
\]

For

\[
k_N=N+R_N(\beta),
\]

equation `(1)` gives

\[
\frac{k_N}{N}
=
e\left(
1-\frac1L
+\frac{\beta}{e}\frac{\ell}{L^2}
+O\!\left(\frac1N\right)
\right),
\tag{10}
\]

hence

\[
\log\frac{k_N}{N}
=
1-\frac1L
+\left(
\frac{\beta}{e}\ell-\frac12
\right)\frac1{L^2}
+O\!\left(\frac{\ell}{L^3}\right).
\tag{11}
\]

Now `\log k_N=L+1+O(1/L)`. Substituting that into `(8)` and expanding the slowly varying factor gives

\[
\log\frac{A(k_N)}{A(N)}
=
\frac1L
+\left(\frac12-\ell\right)\frac1{L^2}
+O\!\left(\frac{\ell^2}{L^3}\right).
\tag{12}
\]

The first-order `1/L` terms in `(11)` and `(12)` cancel. Therefore

\[
\begin{aligned}
H_N(R_N(\beta))
&=\log\frac{p_{k_N}}{p_N}\\
&=\log\frac{k_N}{N}
 +\log\frac{A(k_N)}{A(N)}\\
&=1+
\left(\frac{\beta}{e}-1\right)
\frac{\ell}{L^2}
+O\!\left(\frac{\ell^2}{L^3}\right),
\end{aligned}
\tag{13}
\]

which is `(4)`.

The same expansion brackets the unique prime index at which the physical reach crosses one. Taking

\[
k_N^*
=
e N-e\frac{N}{L}+e\frac{N\ell}{L^2}
\tag{14}
\]

makes the `\ell/L^2` term in `(13)` vanish. Perturbing `k_N^*` by `\pm C N\ell^2/L^3` changes `\log(p_k/p_N)` by `\pm(C/e+o(1))\ell^2/L^3`, while the residual expansion error is `O(\ell^2/L^3)`. For sufficiently large fixed `C`, monotonicity of `p_k` brackets the crossing index and yields `(7)`.

This is a purely classical prime-asymptotic step. Its role here is to calibrate the amount of **successor-label breadth** needed to preserve a fixed physical relation in the logarithmic prime coordinate.

## PF3 blindness below the wall

AF-397 proves the exact locality statement

\[
H_N(R)\le1
\quad\Longrightarrow\quad
\text{every sampled order-three minor in the block is nonnegative.}
\tag{15}
\]

If `\beta<e`, equation `(4)` gives

\[
H_N(R_N(\beta))
=
1-c_\beta\frac{\ell}{L^2}
+O\!\left(\frac{\ell^2}{L^3}\right)
<1
\tag{16}
\]

for some `c_\beta>0` and all sufficiently large `N`. Hence the entire block is PF3-blind to the disconnected curvature support of the AF-395 profile.

The exact count `(6)` makes the geometry transparent. For every `R\le B_N`,

\[
p_{N+R}<e p_N,
\qquad
H_N(R)<1,
\tag{17}
\]

because `e p_N` is not an integer and therefore cannot itself be prime. Thus `B_N` is the last successor depth that remains strictly on the blind side of the physical topology boundary.

## One prime-log mesh beyond the wall still forces detection

AF-397 also proves the exact converse criterion

\[
H_N(R)>1+\Delta_N(R),
\qquad
\Delta_N(R)<\frac14
\quad\Longrightarrow\quad
\text{the block contains a strictly negative order-three minor.}
\tag{18}
\]

No determinant margin bounded away from zero is required: one sampled mesh width of physical overhang beyond the topology wall suffices.

For `R=R_N(\beta)` with `\beta>e`, `(4)` gives

\[
H_N(R)-1
\asymp
\frac{\ell}{L^2}.
\tag{19}
\]

The Baker--Harman--Pintz input already audited in AF-380 and reused in AF-395/AF-397 gives uniformly on these blocks

\[
\Delta_N(R)
=O\!\left(p_N^{-19/40}\right).
\tag{20}
\]

Since `p_N\sim N\log N`,

\[
p_N^{-19/40}
=o\!\left(\frac{\ell}{L^2}\right).
\tag{21}
\]

Therefore `(18)` applies for all sufficiently large `N`. Every third-scale block with `\beta>e` is eventually detecting.

The detector uncertainty remains microscopic compared with the new arithmetic correction. The prime-log mesh shrinks polynomially in `p_N`, whereas the third-scale shift in physical reach is only logarithmically small.

## Representation and fidelity interpretation

The useful object is not the raw successor count `R` by itself. The AF-395/AF-397 detector sees the physical logarithmic reach

\[
H_N(R)=\log(p_{N+R}/p_N),
\]

and the compression replaces that coordinate by the discrete resource `R`. The asymptotic expansion of the primes is therefore the representation map between two resource scales.

At first order, treating `p_n` as proportional to `n` gives the coarse wall `(e-1)N`. The `-eN/\log N` term records the first variation of prime density. The new `+eN\log\log N/\log^2N` term records the next correction needed to keep the same physical topology boundary after compression to successor labels.

This is a concrete instance of Arithmetic Fidelity's compositional rule: a property can survive a compression only if the retained resource is calibrated in the coordinate in which the downstream discriminator is local. A fixed physical reach does not correspond to a fixed or even purely linear combinatorial breadth on the rational-prime source; lower-order source-density corrections remain visible in the recovery budget.

The representation audit also prevents over-interpreting `(5)`. It is not a new prime invariant and does not create a new RH discriminator. It is the asymptotic conversion law for an already identified PF3 topology wall.

## Prior-art and novelty audit

Juan Arias de Reyna and Jérémy Toulisse, **“The n-th prime asymptotically,”** *Journal de Théorie des Nombres de Bordeaux* **25**(3) (2013), 521--555, DOI `10.5802/jtnb.847`, give a modern derivation of the classical full asymptotic expansion of the `n`th prime and explicit control of its terms. Equation `(8)` is a standard low-order specialization.

R. C. Baker, G. Harman, and J. Pintz, **“The Difference Between Consecutive Primes, II,”** *Proceedings of the London Mathematical Society* **83**(3) (2001), 532--562, DOI `10.1112/plms/83.3.532`, supply the short-interval prime theorem used through AF-380 to obtain `(20)`.

The asymptotic inversion leading to `(7)` is classical analytic-number-theory algebra; no novelty is claimed for the coefficient `e` in the log-log correction viewed purely as an expansion of `\pi(e p_N)`. A focused search for fixed-multiple successor-prime asymptotics did not identify a standard theorem coupling that expansion to prime-log Pólya-frequency detection. **No novelty is claimed for the packaged result either.** The durable Arithmetic Fidelity content is the exact composition of classical source-density asymptotics with AF-397's one-mesh topology detector.

## Boundaries and falsification

The theorem is specific to the AF-395 profile and AF-397's physical topology wall at reach one. A different curvature geometry can move the wall or change the required detector pattern.

The two one-sided implications require fixed `\beta<e` or fixed `\beta>e`. At the boundary `\beta=e`, equation `(4)` leaves an uncertainty of order `\ell^2/L^3`; resolving that thinner scale requires one further term of the prime-index inversion and is not claimed here.

The result concerns order-three total positivity. It does not imply that other compression families have the same successor-depth cost, nor that prime provenance survives after the PF3 property has been propagated to a universal continuous translation statement.

The Baker--Harman--Pintz estimate is used only on the detecting side. The blind side follows from the exact physical reach inequality and requires no prime-gap theorem.

No RH consequence is established. The result sharpens the resource cost of exposing a known topology-sensitive PF3 violation on rational-prime logarithmic samples; it does not prove the sampled inequalities required by any RH-equivalent total-positivity program.

## Consequences

AF-397's unresolved `\alpha=e` family now has a sharp next-scale split. The prime-log PF3 detector remains blind below

\[
(e-1)N-eN/\log N+eN\log\log N/\log^2N
\]

and becomes detecting above it once the excess is a fixed nonzero multiple of `N\log\log N/\log^2N`.

More importantly for the line, the result exhibits a hierarchy of **representation-sensitive recovery costs**. The exact physical discriminator stays fixed, but successive corrections in the source's density law reappear as successive terms in the combinatorial breadth required to preserve it. The next live boundary is whether that hierarchy has a useful general formulation for regularly varying or arithmetic sampling sources, rather than whether this one prime asymptotic can be expanded indefinitely.