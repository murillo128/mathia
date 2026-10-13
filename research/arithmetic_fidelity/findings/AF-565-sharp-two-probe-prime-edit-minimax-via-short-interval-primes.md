# AF-565 — Sharp two-probe prime-edit minimax loss via short-interval primes

## Status

EXACT-DERIVED · LITERATURE+DERIVED · ARITHMETIC-FIDELITY · MULTIWAY-IDENTIFICATION · PRIME-TAIL · MINIMAX-SAMPLING · PRIME-GAP-THRESHOLD · MATCHED-CONTROL · NO-GENERAL-NOVELTY-CLAIM

## Claim: the AF-564 two-probe guarantee is unconditionally sharp

Keep exactly the ordered, commonly registered prime-edit critical curves and deterministic additive sup-norm observation-noise model of AF-559, AF-562 and AF-564. For a finite set \(S\) of at least two odd rational-prime edit locations, let \(\varepsilon_k(S)\) be its best \(k\)-sample unique-decoding radius and \(\varepsilon_{\rm full}(S)\) the complete-curve radius, as defined in AF-562. The edited generators themselves are generalized-prime matched controls, not alternative rational-prime systems.

For fixed \(k\ge1\), define
\[
r_k=(3/2)^{1/k},\qquad
u_k=\frac{\log r_k}{r_k-1},\qquad
\vartheta_k=u_k e^{1-u_k},\qquad
\beta_k=3-\frac{3}{r_k}.
\tag{1}
\]
AF-564 already proves, **without a prime-gap hypothesis**, the universal lower bound
\[
\liminf_{P\to\infty}\inf_{\substack{S\subset\{\text{odd primes}\}\\
2\le |S|<\infty,\ \min S\ge P}}
\frac{\varepsilon_k(S)}{\varepsilon_{\rm full}(S)}
\ \ge\ \vartheta_k
\tag{2}
\]
for every fixed \(k\) (indeed with a common error uniform even in varying \(k\)).

**Sharpness under an explicit short-interval hypothesis.** Suppose \(k\ge2\) is fixed and there are constants \(C>0\) and \(0\le\beta<\beta_k\) such that every sufficiently large real \(x\) has a rational prime in \([x,x+C x^\beta]\). Then a sequence of sets \(S_n\), each containing exactly \(2(k+1)\) distinct odd primes, satisfies
\[
\frac{\varepsilon_k(S_n)}{\varepsilon_{\rm full}(S_n)}
\longrightarrow \vartheta_k.
\tag{3}
\]
Consequently the infimum limit in (2) **equals** \(\vartheta_k\) under that hypothesis.

For \(k=2\),
\[
r_2=\sqrt{3/2},\qquad
\beta_2=3-\sqrt6=0.5505102572\ldots .
\]
The unconditional Baker--Harman--Pintz prime-in-short-interval theorem gives the hypothesis with \(\beta=0.525<\beta_2\). Hence, without any unproved gap conjecture,
\[
\boxed{\quad
\lim_{P\to\infty}
\inf_{\substack{S\subset\{\text{odd primes}\}\\
2\le |S|<\infty,\ \min S\ge P}}
\frac{\varepsilon_2(S)}{\varepsilon_{\rm full}(S)}
=\frac{\log\sqrt{3/2}}{\sqrt{3/2}-1}
\exp\left(1-\frac{\log\sqrt{3/2}}{\sqrt{3/2}-1}\right)
=0.994878528675\ldots .
\quad}
\tag{4}
\]
Thus six actual rational-prime *edit locations* asymptotically witness the sharp worst-case two-sample loss of about \(0.51215\%\). This closes the specific \(k=2\) sharpness question left open in AF-564; it is not a claim that the bound is known sharp for every \(k\ge3\).

## Constructing \(k+1\) equally difficult peak scales

Write
\[
D_{p,q}=\sup_{a>0}[\Phi_q(a)-\Phi_p(a)],\qquad
f(u)=u e^{1-u},\qquad c=e^{B_1}.
\]
AF-559 proves both
\[
D_{p,q}=\frac{p^{-2}-q^{-2}}{e\log p}[1+o(1)]
\tag{5}
\]
and global uniform convergence of the normalized response to \(f(ca\log p)\), uniformly over all larger prime edit locations \(q>p\) as \(p\to\infty\).

By the prime number theorem and the average of consecutive prime gaps in \([X,2X]\), choose infinitely many consecutive odd primes \(p_0<q_0\), with
\[
g=q_0-p_0=O(\log p_0),\qquad
d_0=\frac{2g}{e p_0^3\log p_0}.
\tag{6}
\]
The first adjacent-pair margin obeys \(D_{p_0,q_0}\sim d_0\).

Set \(r=r_k\). For each \(1\le j\le k-1\), choose a prime
\(p_j\sim p_0^{r^j}\), and prescribe the positive target gap
\[
\Delta_j=g\left(\frac{p_j}{p_0}\right)^3
\frac{\log p_j}{\log p_0}.
\tag{7}
\]
Because \(r^j<r^k=3/2\) and \(\log g=o(\log p_0)\),
\[
\frac{\Delta_j}{p_j}\longrightarrow0,
\qquad
\frac{\Delta_j}{p_j^\beta}
\asymp g\,p_0^{(3-\beta)r^j-3}\longrightarrow\infty .
\tag{8}
\]
The last limit is valid for **every** \(j\ge1\): its smallest exponent occurs at \(j=1\) and is positive precisely when
\(\beta<3-3/r=\beta_k\).
The short-interval hypothesis, applied at \(x=p_j+\Delta_j\), therefore gives a prime \(q_j>p_j\) with
\[
q_j-p_j=\Delta_j+O(p_j^\beta)=\Delta_j[1+o(1)].
\tag{9}
\]
The near-pair version of (5) now gives
\[
D_{p_j,q_j}\sim
\frac{2\Delta_j}{e p_j^3\log p_j}=d_0,
\qquad 1\le j<k .
\tag{10}
\]

For the last peak use the AF-562 far-pair construction:
\[
Q=\frac{p_0^{3/2}}{2\sqrt g},
\qquad p_k\sim Q,\quad q_k\sim2Q
\tag{11}
\]
with \(p_k,q_k\) odd primes supplied by PNT. Then
\[
D_{p_k,q_k}\sim
\frac{3/(4Q^2)}{e\log Q}\sim d_0,
\qquad \frac{\log p_k}{\log p_0}\longrightarrow\frac32=r^k.
\tag{12}
\]
All the pairs are eventually strictly ordered:
\[
p_0<q_0<p_1<q_1<\cdots<p_k<q_k .
\]
The intermediate *cross-pair* gaps are not bottlenecks. For \(0\le j<k\), (5), \(q_j\sim p_j\), and \(p_{j+1}/q_j\to\infty\) give
\[
\frac{D_{q_j,p_{j+1}}}{d_0}
\asymp \frac{p_0^{3-2r^j}}{g}
\longrightarrow\infty
\quad(r^j<3/2).
\tag{13}
\]
By AF-562's exact adjacent-pair reduction, the full-curve margin of
\[
S=\{p_0,q_0,\ldots,p_k,q_k\}
\]
is therefore
\[
2\varepsilon_{\rm full}(S)=d_0[1+o(1)].
\tag{14}
\]

## The exact \(k\)-probe obstruction

Put \(x=ca\log p_0\). For each of the \(k+1\) bottleneck pairs, (5) and AF-559's *global* normalized-profile theorem yield, uniformly over all \(x>0\),
\[
\frac{\Phi_{q_j}(x/(c\log p_0))-
\Phi_{p_j}(x/(c\log p_0))}{d_0}
=f(r^jx)+o(1),
\qquad 0\le j\le k .
\tag{15}
\]
Uniformity follows because there are a fixed number of pairs, their peak heights are \(d_0[1+o(1)]\), \(\log p_j/\log p_0\to r^j\), and \(f\) decays at both endpoints. The cross-pair responses at every fixed \(x>0\) are \(\gg d_0\), by (13) and the same profile theorem.

We now solve the elementary, but decisive, finite maximin problem:
\[
\boxed{\quad
\sup_{x_1,\ldots,x_k>0}
\min_{0\le j\le k}\max_{1\le \ell\le k}
f(r^j x_\ell)=\vartheta_k .
\quad}
\tag{16}
\]
For the lower bound, take \(x_\ell=u_k/r^{\ell-1}\), \(\ell=1,\ldots,k\).
The sample \(x_\ell\) covers both successive scales \(r^{\ell-1}\) and \(r^\ell\), since
\[
f(u_k)=f(r u_k)=\vartheta_k
\quad\text{by}\quad (r-1)u_k=\log r .
\tag{17}
\]
Every one of the \(k+1\) scales is covered.

For the upper bound, fix \(\theta>\vartheta_k\), \(\theta<1\), and let
\(0<u_-(\theta)<1<u_+(\theta)\) be the two roots of \(f(u)=\theta\).
The ratio \(R(\theta)=u_+(\theta)/u_-(\theta)\) strictly decreases with
\(\theta\), and (17) gives \(R(\vartheta_k)=r\). Thus \(R(\theta)<r\).
One sample \(x\) cannot attain \(f(r^i x)\ge\theta\) and
\(f(r^j x)\ge\theta\) for two distinct indices \(i<j\), since that would require
\(r^{j-i}\le R(\theta)<r\).
Each sample covers at most one of the \(k+1\) scales above level \(\theta\); \(k\) samples cannot cover all of them. This proves (16).

Equation (15) gives the upper bound
\(\limsup\varepsilon_k(S)/\varepsilon_{\rm full}(S)\le\vartheta_k\)
even for arbitrary nonadaptive sample locations, because the discrepancy from the finite profile problem is globally uniform. At the explicit \(k\) samples from (17), every bottleneck pair attains \(\vartheta_k d_0[1+o(1)]\), and each cross pair attains \(\gg d_0\), proving the reverse bound via the exact adjacent-pair formula. This establishes (3). Combining with AF-564 proves the infimum equality and its unconditional \(k=2\) specialization (4). \(\square\)

## Prior art, falsification controls, and limits

Baker, Harman and Pintz (2001), *The Difference Between Consecutive Primes, II*, prove prime occurrence in \([x,x+x^{0.525}]\) for all sufficiently large \(x\) (DOI: 10.1112/plms/83.3.532). The use here is **not** a new prime-gap theorem. The prime-number theorem, AF-559's pairwise response, AF-562's ordered-curve reduction/far-pair construction, and AF-564's universal sampler are likewise established inputs. Equal-peak interval covering and the pigeonhole obstruction are classical maximin-design arguments; the new source-specific consequence is the first unconditional matching \(k=2\) family of actual odd-prime edit locations, plus the explicit exponent threshold for a conditional fixed-\(k\) construction.

The main falsification checks are: verify \(\beta_2=3-\sqrt6>0.525\); check the prescribed intermediate gap is large relative to \(p_1^{0.525}\) but small relative to \(p_1\); check every one of the \(k+1\) peak heights tends to the *same* \(d_0\); verify no cross-pair gap becomes a minimax bottleneck; and distinguish uniform convergence over **all** observation locations (needed for the upper bound) from convergence only at the explicit lower-bound sample points.

Only \(k=2\) is settled unconditionally here; for \(k\ge3\) the declared short-interval hypothesis is not supplied by the Baker--Harman--Pintz exponent, since \(\beta_k<0.525\). The claim concerns a ratio to a shrinking full-curve absolute-noise margin, not uniformly positive noise tolerance. It assumes a known finite candidate set, source-common critical-coordinate registration, and the critical-index limit taken before the prime-edit locations grow. The edits form generalized-prime matched controls and the construction is not by itself a rational-prime versus generalized-prime discriminator, an RH-facing transported recovery bound, or a proof of RH.

## Consequence for Arithmetic Fidelity

AF-564's two-probe guarantee \(0.994878528675\ldots\) is not merely optimal for a continuous covering surrogate: it is the **sharp asymptotic global minimax fraction for the actual discrete odd-prime edit-source class**. The boundary between known sharpness and an unresolved multi-probe construction is now explicit in the allowed prime-gap exponent. The qualitative exact-versus-stable fidelity obstruction is unchanged: even sharp relative sampling can recover only a vanishing source-separation margin.
