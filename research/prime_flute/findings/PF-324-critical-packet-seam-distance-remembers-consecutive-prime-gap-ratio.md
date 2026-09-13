# PF-324 — critical packet seam distance remembers the consecutive prime-gap ratio

**Status:** `EXACT-DERIVED + LITERATURE+DERIVED + ARITHMETIC-GEOMETRIC NONUNIVERSALITY + ROUTE-NARROWING`.

PF-323 moves the PF-322 compactification-critical physical-low packet off the quotient seam. For fixed `0<lambda<1`, its center `tau_{n,lambda}` is defined intrinsically by

\[
s_n\cosh\tau_{n,\lambda}=\lambda,
\qquad
s_n=\frac{h_n+h_{n+1}}2,
\]

and PF-323 proves that every fixed window of radius smaller than `log(1/lambda)` eventually lies strictly inside the cuff cell. The remaining geometric question is where the **actual outgoing cell seam** lies after this critical recentering.

That position is not universal. Put

\[
r_n:=\frac{h_{n+1}}{h_n},
\qquad
D_{n,\lambda}:=\frac{\ell_n}{2}-\tau_{n,\lambda}.
\]

Then PF-001 and the defining equation above give the exact identity

\[
\boxed{
 e^{D_{n,\lambda}}
 =\coth\!\left(\frac{h_n}{4}\right)
 \frac{s_n}{\lambda+\sqrt{\lambda^2-s_n^2}}.
}
\]

Since `h_n,s_n->0`, this yields

\[
\boxed{
D_{n,\lambda}
=\log\frac{1+r_n}{\lambda}+o(1).
}
\]

The same arithmetic parameter appears in the terminal compactification scale itself. PF-001 gives `cosh(ell_n/2)=coth(h_n/2)`, hence

\[
\boxed{
s_n\cosh\frac{\ell_n}{2}
=1+r_n+o(1).
}
\]

Thus PF-323's universal interior profile

\[
s_n\cosh(\tau_{n,\lambda}+x)\longrightarrow\lambda e^x
\]

is terminated by the real cuff seam at an `x`-location asymptotic to

\[
\log\frac{1+r_n}{\lambda},
\]

where the limiting profile has terminal size `1+r_n`. The adjacent logarithmic prime-mesh ratio therefore survives the critical rescaling as a **boundary-location/boundary-scale parameter** before any finite-pant quotient, seam normalization, or physical `L/H` angle is formed.

PF-299 records

\[
h_n=\frac{g_n}{p_{n-1}}(1+o(1)),
\qquad g_n=p_n-p_{n-1},
\]

and Baker--Harman--Pintz gives `g_n/p_{n-1}->0`. Consequently

\[
\boxed{
r_n
=\frac{g_{n+1}}{g_n}(1+o(1)).}
\]

Pintz's theorem on ratios of consecutive prime gaps (source S4) gives subsequences on which `g_{n+1}/g_n->0` and subsequences on which it tends to infinity. Therefore the canonical prime flute contains both regimes

\[
\boxed{
D_{n,\lambda}\longrightarrow\log(1/\lambda)
}
\]

along a subsequence, and

\[
\boxed{
D_{n,\lambda}\longrightarrow\infty
}
\]

along another.

This is the first useful consequence of PF-323 for the downstream projected-angle problem: after critical recentering there is **no single universal finite-pant boundary geometry**. On small-next-gap-ratio subsequences the seam remains at the smallest asymptotically allowed finite distance from the packet. On large-next-gap-ratio subsequences the seam escapes every fixed recentered window, so the same critical packet becomes arbitrarily deep in the cuff interior relative to that outgoing seam.

The result does **not** prove that the completed intrinsic angle is large, nor that the gap ratio is a spectral invariant. The quotient, seam-energy normalization, physical `L/H` projection, and common positive completion can still act nonlocally. What it removes is the assumption that PF-323's critical-window calculation may be followed by one gap-independent local seam model. Any uniform proof of the accepted direct-angle clue must handle both arithmetic boundary regimes.

## Claim

Let `h_n`, `ell_n`, and `s_n=(h_n+h_{n+1})/2` be the canonical prime-flute quantities from PF-001/PF-299. Fix `0<lambda<1`, and for all sufficiently large `n` define

\[
\tau_{n,\lambda}=\operatorname{arcosh}(\lambda/s_n),
\qquad
D_{n,\lambda}=\ell_n/2-\tau_{n,\lambda},
\qquad
r_n=h_{n+1}/h_n.
\]

Then:

1. one has the exact identity
   \[
   \boxed{
   e^{D_{n,\lambda}}
   =\coth(h_n/4)
    \frac{s_n}{\lambda+\sqrt{\lambda^2-s_n^2}};
   }
   \]
2. uniformly along the canonical tail,
   \[
   \boxed{
   D_{n,\lambda}
   =\log\frac{1+r_n}{\lambda}
   +O(h_n^2+s_n^2);
   }
   \]
3. the scaled compactification coefficient at the outgoing seam obeys
   \[
   \boxed{
   s_n\cosh(\ell_n/2)
   =1+r_n+o(1);
   }
   \]
4. using PF-299's logarithmic-gap asymptotic,
   \[
   \boxed{
   r_n=\frac{g_{n+1}}{g_n}(1+o(1));
   }
   \]
5. by Pintz's consecutive-gap-ratio theorem there are subsequences with `r_n->0` and with `r_n->infinity`, and therefore respectively
   \[
   D_{n,\lambda}\to\log(1/\lambda)
   \quad\text{and}\quad
   D_{n,\lambda}\to\infty.
   \]

In the PF-323 recentered coordinate `x=tau-tau_{n,lambda}`, the left half-cell center lies at `x=-tau_{n,lambda}->-infinity`, while the outgoing seam lies at `x=D_{n,lambda}`. Hence the critical local domain has at least two genuinely different arithmetic subsequential geometries: a finite terminal boundary and an escaping terminal boundary.

## 1. Exact seam location after critical recentering

PF-001 gives

\[
e^{-\ell_n/2}=\tanh(h_n/4),
\]

so

\[
e^{\ell_n/2}=\coth(h_n/4).
\]

PF-323 defines the critical point by `cosh tau_{n,lambda}=lambda/s_n`. For `x>1`,

\[
e^{-\operatorname{arcosh}x}
=x-\sqrt{x^2-1}
=\frac1{x+\sqrt{x^2-1}}.
\]

Substituting `x=lambda/s_n` gives

\[
e^{-\tau_{n,\lambda}}
=\frac{s_n}{\lambda+\sqrt{\lambda^2-s_n^2}}.
\]

Multiplication by `e^{ell_n/2}` proves the exact formula for `e^{D_{n,lambda}}`.

Now use the elementary tail expansions

\[
\coth(h_n/4)
=\frac4{h_n}\bigl(1+O(h_n^2)\bigr)
\]

and, for fixed `lambda`,

\[
\lambda+\sqrt{\lambda^2-s_n^2}
=2\lambda\bigl(1+O(s_n^2)\bigr).
\]

Because `2s_n=h_n+h_{n+1}`, one obtains

\[
e^{D_{n,\lambda}}
=\frac{1+r_n}{\lambda}
\bigl(1+O(h_n^2+s_n^2)\bigr),
\]

and taking logarithms proves the claimed asymptotic. The error is uniform with respect to the size of `r_n`: it is expressed only through `h_n,s_n->0`.

## 2. The same ratio is the terminal scaled compactification weight

PF-322 rewrites PF-001's cuff identity as

\[
\cosh(\ell_n/2)=\coth(h_n/2).
\]

Therefore

\[
s_n\cosh(\ell_n/2)
=s_n\coth(h_n/2).
\]

Since

\[
\coth(h_n/2)=\frac2{h_n}+O(h_n),
\]

we obtain

\[
\begin{aligned}
s_n\coth(h_n/2)
&=\frac{2s_n}{h_n}+O(s_nh_n)\\
&=1+r_n+O(h_n^2+h_nh_{n+1}).
\end{aligned}
\]

Both error terms tend to zero. Thus the outgoing endpoint of PF-323's critical profile retains the same adjacent-mesh ratio that determines its recentered location.

This also checks the internal consistency of the scaling. If `r_n` stays bounded along a subsequence, then PF-323's local profile `lambda e^x` evaluated at `x=D_{n,lambda}` tends to `1+r`, exactly the terminal scale above. If `r_n->infinity`, both the terminal location and terminal scale diverge.

## 3. The mesh ratio inherits the consecutive prime-gap ratio

PF-299 records the already-audited asymptotic

\[
h_n=\frac{g_n}{p_{n-1}}(1+o(1)).
\]

Applied at `n+1`,

\[
h_{n+1}=\frac{g_{n+1}}{p_n}(1+o(1)).
\]

Hence

\[
\frac{h_{n+1}}{h_n}
=\frac{g_{n+1}}{g_n}
\frac{p_{n-1}}{p_n}(1+o(1)).
\]

The unconditional short-interval bound already used in PF-299 implies `g_n/p_{n-1}->0`, so `p_{n-1}/p_n->1`. This proves

\[
r_n=\frac{g_{n+1}}{g_n}(1+o(1)).
\]

Source S4 records Pintz's theorem that ratios of consecutive prime gaps are infinitely often arbitrarily small and arbitrarily large. Multiplicative `1+o(1)` does not change either regime. The two asserted subsequences for `D_{n,lambda}` follow immediately.

## 4. Consequence for the completed projected-angle test

PF-323 already shows that the critical packet can be placed a fixed positive distance away from the seam. PF-324 strengthens the geometry of that statement in the only direction relevant to the next finite-pant calculation.

There are two adversarial regimes to test separately:

- **finite-boundary regime:** along `r_n->0`, the outgoing seam remains at `x=log(1/lambda)+o(1)` in the critical coordinate. Any cancellation created by the quotient/seam normalization is maximally exposed here;
- **escaping-boundary regime:** along `r_n->infinity`, the outgoing seam leaves every fixed critical window. Any proposed cancellation that is genuinely localized to a bounded neighborhood of that seam cannot be inferred uniformly from the same local model on this subsequence.

The second statement is a test prescription, not an angle theorem. The finite-pant completion and energy normalization may be nonlocal, so seam escape does not by itself imply survival of the PF-323 packet. It does, however, provide a much sharper falsification family: a proof of uniform `O(s_n^{1+epsilon})` angle decay must explain what suppresses the critical packet even when the outgoing seam is arbitrarily far away in its natural rescaled coordinate.

Conversely, if the completed angle has different asymptotics in the two regimes, that would be a concrete mechanism by which **prime ordering survives beyond a scalar relabeling**. PF-324 does not establish such a difference; it establishes only the arithmetic dependence of the input geometry on which that comparison should be made.

## 5. Prior art and novelty audit

The ingredients are not new individually. PF-001's tight-flute cuff identity comes from the standard zero-twist tight-flute geometry recorded under source S1; the elementary `arcosh` and hyperbolic expansions are classical; PF-299 supplies the already-audited logarithmic-gap asymptotic; and Pintz's theorem on ratios of consecutive prime gaps is recorded under source S4. A fresh source check confirms that Pintz's result explicitly answers the Erdős question by proving that consecutive prime-gap ratios are infinitely often arbitrarily small and arbitrarily large.

No standalone novelty is claimed for any of those facts. The project-specific result is their exact composition at PF-323's critical compactification scale: the adjacent prime-gap ratio becomes the terminal boundary position and scale seen by the recentered physical-low packet. The literature audit found no external theorem asserting this prime-flute critical-rescaling statement, nor would one be expected independently of this construction.

## 6. Boundaries and falsification

1. **Geometry before angle.** `D_{n,lambda}` is a cuff-cell/seam location in the critical coordinate. It is not a lower bound for the completed intrinsic `L/H` angle.
2. **Not yet a spectral invariant.** Dependence of the recentered local geometry on `r_n` does not prove that the spectrum, scattering matrix, determinant, or any RH-relevant invariant recovers `r_n`.
3. **No universal seam-local model.** The theorem rules out replacing the actual outgoing seam by one fixed recentered boundary position uniformly in `n`; it does not rule out a more global gap-independent cancellation mechanism.
4. **No conjectural prime-gap law.** The existence of the two extreme ratio subsequences uses the audited Pintz theorem; no Cramér-type model or unproved distribution assumption enters.
5. **Indexing matters.** The relevant ratio is the outgoing increment `h_{n+1}/h_n`, asymptotic to `g_{n+1}/g_n`. Reversing the orientation exchanges the corresponding ratio.
6. **No RH conclusion.** This finding sharpens one local direct-angle test only.

A refutation would have to break the exact exponential identity for `D_{n,lambda}`, PF-001's cuff law, PF-299's mesh definition/asymptotic, or the cited consecutive-gap-ratio theorem.

## Consequence for the research line

The accepted direct-angle clue should use PF-323's **interior critical packets**, not only the seam-centered PF-322 family, and should separate the projected-angle calculation into the two arithmetic regimes above. The large-gap-ratio subsequence is particularly diagnostic: it sends the quotient seam to infinity in every fixed critical window while preserving the order-one compactification-critical packet profile. If the completed physical angle still gains a superlinear seam power there, the mechanism must be identified beyond a merely bounded-distance seam interaction. If it does not, PF-318's Hilbert--Schmidt fallback should be tested on the same arithmetic subsequence.